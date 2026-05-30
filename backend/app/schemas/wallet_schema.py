from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class CreateWallet(BaseModel):
    name: str
    balance: float
    currency: str

class UpdateWallet(BaseModel):
    # userName: str  //it has to show user name here
    name: Optional[str | None] = None
    balance: Optional[float | None] = None
    currency: Optional[str | None] = None