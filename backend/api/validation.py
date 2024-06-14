from pydantic import BaseModel

class SpazaInfo(BaseModel):
    spaza_name: str
    spaza_id: int
    spaza_reg_no: int
    spaza_email: str
    spaza_password: str