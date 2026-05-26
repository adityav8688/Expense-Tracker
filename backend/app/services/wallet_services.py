from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from app.models.users_model import Users
from app.models.wallets_model import Wallets
from app.schemas.wallet_schema import CreateWallet, WalletInfo

def wallets_list(db: Session, uid: int):
    wallets = db.query(Wallets).filter(Wallets.user_id == uid).all()

    return wallets

def wallet_info(id: int, db: Session, uid: int):
    wallet = db.query(Wallets).filter(Wallets.user_id == uid, Wallets.id == id).first()

    if not wallet: 
        raise HTTPException(status_code=404, detail="some error...")
    
    user = db.query(Users).filter(Users.id == wallet.user_id).first()

    return { 
        "User Name": user.name,
        "Wallet Name": wallet.name,
        "balance" : wallet.balance,
        "currency" : wallet.currency,
        "created at" : wallet.created_at
    }

def create_wallet(wallet: CreateWallet, db: Session, uid: int):
    add_wallet = Wallets(
        user_id = uid,
        name = wallet.name,
        balance = wallet.balance,
        currency = wallet.currency
    )
    db.add(add_wallet)
    db.commit()
    db.refresh(add_wallet)

    return {"message": "Wallet added."}

def update_wallet(wallet: CreateWallet, id: int, db: Session, uid: int):
    ex_wallet = db.query(Wallets).filter(Wallets.user_id == uid, Wallets.id == id).first()

    if not ex_wallet:
        raise HTTPException(status_code=404, detail=f"Wallet with {uid} not found.")
    
    ex_wallet.name = wallet.name
    ex_wallet.balance = wallet.balance
    ex_wallet.currency = wallet.currency
    ex_wallet.created_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(ex_wallet)

    return {"message": "Wallet details Updated."}

def remove_wallet(id: int, db: Session, uid: int):
    del_wallet = db.query(Wallets).filter(Wallets.user_id == uid, Wallets.id == id).first()

    if not del_wallet:
        raise HTTPException(status_code=404, detail=f"There is no record to delete at {uid}")
    
    db.delete(del_wallet)
    db.commit()

    return {"message" : "Wallet Deleted."}