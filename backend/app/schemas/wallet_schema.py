from pydantic import BaseModel, Field
from datetime import datetime

class CreateWallet(BaseModel):
    name: str
    balance: float
    currency: str

class WalletInfo(BaseModel):
    # userName: str  //it has to show user name here
    name: str
    balance: float
    currency: str