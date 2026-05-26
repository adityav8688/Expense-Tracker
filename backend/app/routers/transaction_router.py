from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.core.security import require_role
from app.schemas.transaction_schema import CreateTransaction, TransactionInfo, UpdateTransaction
from app.services.transaction_services import *

transaction_router = APIRouter(prefix="/transaction")

class details():
    db: Session = Depends(get_db)
    role: dict = Depends(require_role("user"))

@transaction_router.get("/", response_model=list[TransactionInfo])
def get_transactions(db = details.db , role = details.role):
    return list_transactions(db, int(role["user_id"]))

@transaction_router.post("/")
def post_transaction(transaction: CreateTransaction, db = details.db, role = details.role):

    return create_transaction(transaction, db, int(role["user_id"]))

@transaction_router.patch("/{id}")
def patch_transaction(id: int , transaction_update: UpdateTransaction, db = details.db, role = details.role):
    return update_transaction(id, transaction_update, db, int(role["user_id"]))

@transaction_router.delete("/{id}")
def delete_transaction(id: int, db = details.db, role = details.role):
    return remove_transaction(id, db, int(role["user_id"]))