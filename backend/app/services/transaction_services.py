from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select

from app.models.transactions_model import Transactions
from app.models.categories_model import Categories
from app.models.wallets_model import Wallets
from app.schemas.transaction_schema import CreateTransaction, UpdateTransaction, TransactionInfo

async def list_transactions(db: AsyncSession, uid: int):
    try:
        query = await db.execute(select(Transactions).where(Transactions.user_id == uid))
        transactions = query.scalars().all()
        return transactions
    except (SQLAlchemyError) as e:
        raise HTTPException(status_code=500, detail=str(e))

async def create_transaction(transaction: CreateTransaction, db: AsyncSession, uid: int):
    try:
        c_query = await db.execute(select(Categories).where(Categories.user_id == uid, Categories.id == transaction.category_id))
        w_query = await db.execute(select(Wallets).where(Wallets.user_id == uid, Wallets.id == transaction.wallet_id))
        category = c_query.scalar_one_or_none()
        wallet = w_query.scalar_one_or_none()

        if not category:
            raise HTTPException(status_code=404, detail="Category Not Found")

        if not wallet:
            raise HTTPException(status_code=404, detail="Wallet Not Found")
        
        new_transaction = Transactions(
            user_id = uid,
            category_id = category.id,
            wallet_id = wallet.id,
            type = transaction.type,
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

        await db.commit()
        await db.refresh(new_transaction)
        await db.refresh(wallet)

        return new_transaction
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

async def update_transaction(id: int, transaction_update: UpdateTransaction, db: AsyncSession, uid: int):
    try:
        query = await db.execute(select(Transactions).where(Transactions.user_id == uid, Transactions.id == id))
        ex_transaction = query.scalar_one_or_none()

        if not ex_transaction:
            raise HTTPException(status_code=404, detail="Transaction not found")
        
        if transaction_update.category_id:
            c_query = await db.execute(select(Categories).where(Categories.id == transaction_update.category_id))
            category = c_query.scalar_one_or_none()
            if not category:
                raise HTTPException(status_code=404, detail="Category not found")
        
        if transaction_update.wallet_id:
            w_query = await db.execute(select(Wallets).where(Wallets.id == transaction_update.wallet_id))
            wallet = w_query.scalar_one_or_none()
            if not wallet:
                raise HTTPException(status_code=404, detail="wallet not found")
            
        update_data = transaction_update.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(ex_transaction, key, value)
        
        await db.commit()
        await db.refresh(ex_transaction)

        return ex_transaction
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

async def remove_transaction(id: int, db: AsyncSession, uid: int):
    try:
        query = await db.execute(select(Transactions).where(Transactions.user_id == uid, Transactions.id == id))
        ex_transaction = query.scalar_one_or_none()

        if not ex_transaction:
            raise HTTPException(status_code=404, detail="transaction not found")
        
        w_query = await db.execute(select(Wallets).where(Wallets.user_id == uid, Wallets.id == Transactions.wallet_id))
        wallet = w_query.scalar_one_or_none()
        
        if ex_transaction.type == "expense":
            wallet.balance += ex_transaction.amount
        else: 
            wallet.balance -= ex_transaction.amount
        
        await db.delete(ex_transaction)
        await db.commit()
        return {
            "message": "Transaction Deleted",
            "transaction": ex_transaction
        } 
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))