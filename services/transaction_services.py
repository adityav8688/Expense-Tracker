from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from models.transactions_model import Transactions
from models.categories_model import Categories
from models.wallets_model import Wallets
from schemas.transaction_schema import CreateTransaction, UpdateTransaction, TransactionInfo

def list_transactions(db: Session, uid: int):
    transactions = db.query(Transactions).filter(Transactions.user_id == uid).all()
    return transactions

def create_transaction(transaction: CreateTransaction, db: Session, uid: int):
    category = db.query(Categories).filter(Categories.user_id == uid, Categories.id == transaction.category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category Not Found")
    
    wallet = db.query(Wallets).filter(Wallets.user_id == uid, Wallets.id == transaction.wallet_id).first()

    if not wallet:
        raise HTTPException(status_code=404, detail="Wallet Not Found")
    
    new_transaction = Transactions(
        user_id = uid,
        category_id = category.id,
        wallet_id = wallet.id,
        type = category.type,
        amount = transaction.amount,
        title = transaction.title,
        description = transaction.description,
        transaction_date = transaction.transaction_date
    )

    db.add(new_transaction)

    if category.type == "expense":
        wallet.balance -= transaction.amount
    else:
        wallet.balance += transaction.amount

    db.commit()
    db.refresh(new_transaction)
    db.refresh(wallet)

    return new_transaction

def update_transaction(id: int, transaction_update: UpdateTransaction, db: Session, uid: int):
    ex_transaction = db.query(Transactions).filter(Transactions.user_id == uid, Transactions.id == id).first()

    if not ex_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    if transaction_update.category_id:
        category = db.query(Categories).filter(Categories.id == transaction_update.category_id).first()
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
    
    if transaction_update.wallet_id:
        wallet = db.query(Wallets).filter(Wallets.id == transaction_update.wallet_id).first()
        if not wallet:
            raise HTTPException(status_code=404, detail="wallet not found")
        
    update_data = transaction_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(ex_transaction, key, value)
    
    db.commit()
    db.refresh(ex_transaction)

    return ex_transaction

def remove_transaction(id: int, db: Session, uid: int):
    ex_transaction = db.query(Transactions).filter(Transactions.user_id == uid, Transactions.id == id).first()

    if not ex_transaction:
        raise HTTPException(status_code=404, detail="transaction not found")
    
    wallet = db.query(Wallets).filter(Wallets.user_id == uid, Wallets.id == Transactions.wallet_id).first()
    
    if ex_transaction.type == "expense":
        wallet.balance += ex_transaction.amount
    else: 
        wallet.balance -= ex_transaction.amount
    
    db.delete(ex_transaction)
    db.commit()
    return {
        "message": "Transaction Deleted",
        "transaction": ex_transaction
    } 
