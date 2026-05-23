from sqlalchemy import (
    Column, Integer, String,
    DateTime, ForeignKey,
    Float
)
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime, timezone
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"


class Users(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    email = Column("email", String, unique=True, nullable=False)
    password = Column("password", String, nullable=False)
    created_on = Column("created_on", DateTime, default=datetime.now(timezone.utc))
    logged_on = Column("logged_on", DateTime, default=datetime.now(timezone.utc))
    role = Column("role", String, default=UserRole.USER)

    categories = relationship("Categories", back_populates="user")
    wallets = relationship("Wallets", back_populates="user")
    transaction = relationship("Transactions", back_populates="user")