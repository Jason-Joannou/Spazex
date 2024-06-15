from pydantic import BaseModel

class SpazaInfo(BaseModel):
    spaza_name: str
    spaza_reg_no: int
    spaza_email: str
    spaza_password: str
    spaza_loyalty_no: str

class LoanApplication(BaseModel):
    applicant_name: str
    applicant_id: int
    application_amount: float
