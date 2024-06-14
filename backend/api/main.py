from fastapi import FastAPI, Query, HTTPException, Response, Depends
from sqlalchemy import text
from contextlib import asynccontextmanager
import logging
import bcrypt
import json
from database.sql_connection import SQLiteConnection
from .validation import SpazaInfo

db_conn = SQLiteConnection(database="./test_db.db")

def get_db_session():
    db = db_conn.get_session()
    try:
        yield db
    finally:
        db.close()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    response = db_conn.test_connection()
    if response["connection_status"] == "incomplete":
        raise Exception(response["message"])
    yield
    # Shutdown
    if db_conn._engine:
        db_conn._engine.dispose()
        logging.info("Database connection closed.")

app = FastAPI(lifespan=lifespan)

@app.get('/')
async def root(): # Need to establish connection to database on connection to site
    return {"connection_status": 200}

@app.post("/register_spaza/")
def register_user(shop: SpazaInfo, db=Depends(get_db_session)):
    try:
        # Start a transaction
        with db.begin():
            # Check if the username already exists
            query_username = text("SELECT id FROM users WHERE username = :username")
            result_username = db.execute(query_username, {"username": shop.spaza_name}).fetchone()
            if result_username:
                raise HTTPException(status_code=400, detail="Username already exists")
            
            # Check if the email already exists
            query_email = text("SELECT id FROM users WHERE email = :email")
            result_email = db.execute(query_email, {"email": shop.spaza_email}).fetchone()
            if result_email:
                raise HTTPException(status_code=400, detail="Email already exists")
            
            # Hash the password
            hashed_password = bcrypt.hashpw(shop.spaza_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
            # Insert the user into the database
            query_insert = text("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)")
            db.execute(query_insert, {"username": shop.spaza_name, "email": shop.spaza_email, "password": hashed_password})
            
            db.commit()
        
        return {"message": "User registered successfully"}
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
