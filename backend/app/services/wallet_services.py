from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timezone

from app.models.users_model import Users
from app.models.wallets_model import Wallets
from app.schemas.wallet_schema import CreateWallet, UpdateWallet

async def wallets_list(db: AsyncSession, uid: int):
    try:
        query = await db.execute(select(Wallets).where(Wallets.user_id == uid))
        wallets = query.scalar_one_or_none()

        return wallets
    except (SQLAlchemyError) as e:
        raise HTTPException(status_code=500, detail=str(e))

async def wallet_info(id: int, db: AsyncSession, uid: int):
    try:
        query = await db.execute(select(Wallets).where(Wallets.user_id == uid, Wallets.id == id))
        wallet = query.scalar_one_or_none()

        if not wallet: 
            raise HTTPException(status_code=404, detail="some error...")
        
        u_query = await db.execute(select(Users).where(Users.id == wallet.user_id))
        user = u_query.scalar_one_or_none()

        return { 
            "User Name": user.name,
            "Wallet Name": wallet.name,
            "balance" : wallet.balance,
            "currency" : wallet.currency,
            "created at" : wallet.created_at
        }
    except(SQLAlchemyError) as e:
        raise HTTPException(status_code=500, detail=str(e))

async def create_wallet(wallet: CreateWallet, db: AsyncSession, uid: int):
    try:
        query = await db.execute(select(Wallets).where(Wallets.user_id == uid, Wallets.name == wallet.name))
        ex_wallet = query.scalar_one_or_none()

        if ex_wallet:
            raise HTTPException(status_code=400, detail=f"There is already a Wallet with {wallet.name}.")
        
        add_wallet = Wallets(
            user_id = uid,
            name = wallet.name,
            balance = wallet.balance,
            currency = wallet.currency
        )

        db.add(add_wallet)
        await db.commit()
        await db.refresh(add_wallet)

        return wallet
    except (SQLAlchemyError) as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

async def update_wallet(wallet: UpdateWallet, id: int, db: AsyncSession, uid: int):
    try:
        query = await db.execute(select(Wallets).where(Wallets.user_id == uid, Wallets.id == id))
        ex_wallet = query.scalar_one_or_none()

        if not ex_wallet:
            raise HTTPException(status_code=404, detail=f"Wallet with {uid} not found.")
        
        updated_data = wallet.model_dump(exclude_unset=True)

        for key, value in updated_data.items():
            setattr(ex_wallet, key, value)

        ex_wallet.created_at = datetime.now(timezone.utc)

        await db.commit()
        await db.refresh(ex_wallet)

        return ex_wallet
    except (SQLAlchemyError) as e: 
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

async def remove_wallet(id: int, db: AsyncSession, uid: int):
    try:
        query = await db.execute(select(Wallets).where(Wallets.user_id == uid, Wallets.id == id))
        del_wallet = query.scalar_one_or_none()

        if not del_wallet:
            raise HTTPException(status_code=404, detail=f"There is no record to delete at {uid}")
        
        await db.delete(del_wallet)
        await db.commit()

        return {"message" : "Wallet Deleted."}
    except (SQLAlchemyError) as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))