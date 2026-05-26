from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.core.security import require_role
from app.models.wallets_model import Wallets
from app.services.wallet_services import *
from app.schemas.wallet_schema import CreateWallet, WalletInfo

wallet_router = APIRouter(prefix="/wallet")

@wallet_router.get("/", response_model=list[CreateWallet])
def get_wallets(db: Session = Depends(get_db), role = Depends(require_role("user"))):
    return wallets_list(db, int(role["user_id"]))

@wallet_router.get("/info/{id}")
def get_wallet_info(info_id = id, db: Session = Depends(get_db), role = Depends(require_role("user"))):
    return wallet_info(info_id, db, int(role["user_id"]))

@wallet_router.post("/")
def post_wallet(wallet: CreateWallet, db: Session = Depends(get_db), role = Depends(require_role("user"))):
    return create_wallet(wallet, db, int(role["user_id"]))

@wallet_router.put("/{id}")
def put_wallet(wallet: CreateWallet, put_id = id, db: Session = Depends(get_db), role = Depends(require_role("user"))):
    return update_wallet(wallet, put_id, db, int(role["user_id"]))

@wallet_router.delete("/{id}")
def delete_wallet(del_id = id, db: Session = Depends(get_db), role = Depends(require_role("user"))):
    return remove_wallet(del_id, db, int(role["user_id"]))