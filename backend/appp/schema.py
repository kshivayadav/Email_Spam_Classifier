from pydantic import BaseModel

class sms_input(BaseModel):
    message:str