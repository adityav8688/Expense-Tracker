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
    description: str
    transaction_date: date 

class CreateTransaction(BaseModel):
    categoryId: int
    walletId: int
    type: str
    amount: float
    title: str
    description: Optional[str | None]
    transaction_date: Optional[date | None] = date.today()

class UpdateTransaction(BaseModel): 
    # category: Optional[str] = None
    # wallet: Optional[str] = None
    amount: Optional[float] = None
    title: Optional[str] = None
    description: Optional[str] = None
    transaction_date: Optional[date] = None