from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class exptype(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"

class CategoryInfo(BaseModel):
    name: str
    type: exptype
    color: str|None
    icon: str|None
    created_at: datetime

class CreateCategory(BaseModel):
    name: str
    type: exptype
    color: str|None
    icon: str|None