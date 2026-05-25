from sqlalchemy import (
    Column, Integer, String,
    DateTime, ForeignKey,
    Float
)
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime, timezone

class Wallets(Base):
    __tablename__ = "wallets"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    balance = Column(Float)
    currency = Column(String)
    created_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))

    user = relationship("Users", back_populates="wallets")
    transaction = relationship("Transactions", back_populates="wallet")