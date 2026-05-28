from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import require_role
from app.schemas.transaction_schema import CreateTransaction, TransactionInfo, UpdateTransaction
from app.services.transaction_services import *

transaction_router = APIRouter(prefix="/transaction")

class details():
    db: Session = Depends(get_db)
    role: dict = Depends(require_role("user"))

@transaction_router.get("/", response_model=list[TransactionInfo])
async def get_transactions(db = details.db , role = details.role):
    try:
        return await list_transactions(db, int(role["user_id"]))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@transaction_router.post("/")
async def post_transaction(transaction: CreateTransaction, db = details.db, role = details.role):
    try:
        return await create_transaction(transaction, db, int(role["user_id"]))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@transaction_router.patch("/{id}")
async def patch_transaction(id: int , transaction_update: UpdateTransaction, db = details.db, role = details.role):
    try:
        return await update_transaction(id, transaction_update, db, int(role["user_id"]))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@transaction_router.delete("/{id}")
async def delete_transaction(id: int, db = details.db, role = details.role):
    try:
        return await remove_transaction(id, db, int(role["user_id"]))  
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))