from sqlalchemy import (
    Column, Integer, String,
    DateTime, ForeignKey,
    Float, Enum as SQLEnum
)
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime, timezone
from enum import Enum

class type(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"


class Transactions(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    wallet_id = Column(Integer, ForeignKey("wallets.id"))
    type = Column(SQLEnum(type), default=type.INCOME)
    amount = Column(Float)
    title = Column(String)
    description = Column(String)
    transaction_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    user = relationship("Users", back_populates="transaction")
    category = relationship("Categories", back_populates="transaction")
    wallet = relationship("Wallets", back_populates="transaction")