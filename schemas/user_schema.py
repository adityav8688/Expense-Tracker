from pydantic import BaseModel, Field, EmailStr, PastDatetime
from datetime import datetime, timezone

class UserCreate(BaseModel):
    name: str = Field(max_length=50)
    email: EmailStr
    password: str = Field(min_length=4)

class UserInfo(BaseModel):
    name: str
    email: EmailStr
    created_on : PastDatetime
    role: str

