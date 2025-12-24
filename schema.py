from pydantic import BaseModel
from typing import Annotated

class sms_input(BaseModel):
    message:str