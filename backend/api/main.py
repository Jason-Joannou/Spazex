from fastapi import FastAPI, Query, HTTPException, Response, Depends
from sqlalchemy import text
from contextlib import asynccontextmanager
import logging
import bcrypt
from database.sql_connection import SQLiteConnection
from .validation import SpazaInfo
from .utility import generate_loyalty_number

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

# Need to fix spaza registration api call
@app.post("/register_spaza")
def register_user(shop: SpazaInfo, db=Depends(get_db_session)):
    try:
        # Start a transaction
        with db.begin():
            # Check if registration exists
            query_reg = text("SELECT id FROM SPAZASHOPS WHERE registration_id = :registration")
            result_reg = db.execute(query_reg, {"registration": shop.spaza_reg_no}).fetchone()
            if result_reg:
                raise HTTPException(status_code=400, detail="Registration Number already exists")
            
            # Check if the username already exists
            query_username = text("SELECT id FROM SPAZASHOPS WHERE name = :name")
            result_username = db.execute(query_username, {"name": shop.spaza_name}).fetchone()
            if result_username:
                raise HTTPException(status_code=400, detail="SPAZASHOP Name already exists")
            
            # Check if the email already exists
            query_email = text("SELECT id FROM SPAZASHOPS WHERE email = :email")
            result_email = db.execute(query_email, {"email": shop.spaza_email}).fetchone()
            if result_email:
                raise HTTPException(status_code=400, detail="SPAZASHOP Email already exists")
            
            # Loyalty Number
            loyal_no = generate_loyalty_number(shop_name=shop.spaza_name, registration_number=shop.spaza_reg_no)
            
            # Hash the password
            hashed_password = bcrypt.hashpw(shop.spaza_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
            # Insert the user into the database
            query_insert = text("INSERT INTO SPAZASHOPS (name, email, registration_id, loyalty_no, password) VALUES (:name, :email, :registration, :loyalty, :password)")
            db.execute(query_insert, {"name": shop.spaza_name, "email": shop.spaza_email, "registration":shop.spaza_reg_no , "loyalty": loyal_no, "password": hashed_password})
            
            db.commit()
        
        return {"message": "Shop registered successfully"}
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post("/spaza_login")
def login_user(shop: SpazaInfo, db=Depends(get_db_session)):
    try:
        query = text("SELECT * FROM SPAZASHOPS WHERE registration_id = :registration")
        result = db.execute(query, {"registration": shop.spaza_reg_no}).fetchone()
        
        if result and bcrypt.checkpw(shop.spaza_password.encode('utf-8'), result[5].encode('utf-8')):  # Assuming password is the 5th column (index 4)
            return {"message": "Login successful"}
        else:
            raise HTTPException(status_code=401, detail="Invalid registration or password for Spaza shop")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
