from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from typing import Optional

class exptype(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"

class CategoryInfo(BaseModel):
    name: Optional[str | None] = None
    type: Optional[exptype | None] = None
    color: Optional[str | None] = None
    icon: Optional[str | None] = None
    created_at: Optional[datetime | None] = None

class CreateCategory(BaseModel):
    name: str
    type: exptype
    color: str|None
    icon: str|None