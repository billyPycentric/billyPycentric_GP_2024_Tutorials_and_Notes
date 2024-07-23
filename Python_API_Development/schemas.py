from typing import Optional
from pydantic import BaseModel, EmailStr



class Person(BaseModel):
    name : str
    surname: str
    age : str
    employable : bool
    qualification: str
    failed_marriages :Optional[int] = 1

class PersonLogin(BaseModel):
    email:EmailStr
    password:str    