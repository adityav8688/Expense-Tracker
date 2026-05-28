from sqlalchemy import (
    Column, Integer, String,
    DateTime, ForeignKey,
    Float, Enum as SQLEnum
)
from sqlalchemy.orm import relationship
from app.core.database import Base
from datetime import datetime, timezone
from enum import Enum

class type(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"

class Categories(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    type = Column(SQLEnum(type), default=type.INCOME)
    color = Column(String)
    icon = Column(String)
    created_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))

    user = relationship("Users", back_populates="categories")
    transaction = relationship("Transactions", back_populates="category")