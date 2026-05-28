from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import require_role
from app.services.wallet_services import *
from app.schemas.wallet_schema import CreateWallet, WalletInfo

wallet_router = APIRouter(prefix="/wallet")

@wallet_router.get("/", response_model=list[CreateWallet])
async def get_wallets(db: Session = Depends(get_db), role = Depends(require_role("user"))):
    try:
        return await wallets_list(db, int(role["user_id"]))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@wallet_router.get("/info/{id}")
async def get_wallet_info(info_id = id, db: Session = Depends(get_db), role = Depends(require_role("user"))):
    try:
        return await wallet_info(info_id, db, int(role["user_id"]))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@wallet_router.post("/")
async def post_wallet(wallet: CreateWallet, db: Session = Depends(get_db), role = Depends(require_role("user"))):
    try:
        return await create_wallet(wallet, db, int(role["user_id"]))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@wallet_router.put("/{id}")
async def put_wallet(wallet: CreateWallet, put_id = id, db: Session = Depends(get_db), role = Depends(require_role("user"))):
    try:
        return await update_wallet(wallet, put_id, db, int(role["user_id"]))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@wallet_router.delete("/{id}")
async def delete_wallet(del_id = id, db: Session = Depends(get_db), role = Depends(require_role("user"))):
    try:
        return await remove_wallet(del_id, db, int(role["user_id"]))
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))