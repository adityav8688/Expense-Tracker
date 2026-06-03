from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, date
from enum import Enum

class exptype(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"

class TransactionInfo(BaseModel):
    type: exptype
    amount: float
    title: str
    description: str | None
    transaction_date: date | None

class CreateTransaction(BaseModel):
    category: Optional[str | None] = None
    wallet: str
    type: str
    amount: float
    title: str
    description: str | None
    transaction_date: Optional[date] = None

class UpdateTransaction(BaseModel):
    # category: Optional[str] = None
    # wallet: Optional[str] = None
    amount: Optional[float] = None
    title: Optional[str] = None
    description: Optional[str] = None
    transaction_date: Optional[date] = None