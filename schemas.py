from typing import Optional
from pydantic import BaseModel, EmailStr

class PersonCreate(BaseModel):
    name: str
    age: int
    email: EmailStr

class PersonRead(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr

    class Config:
        orm_mode = True

class PersonUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[EmailStr] = None

