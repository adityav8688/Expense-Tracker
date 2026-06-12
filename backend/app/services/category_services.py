from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, func, delete
from datetime import datetime, timezone
from typing import Annotated

from app.models.categories_model import Categories
from app.models.transactions_model import Transactions
from app.schemas.category_schema import CreateCategory, CategoryInfo

async def fetch_categories(db: AsyncSession, uid:int):
    try:
        categories = await db.execute(select(Categories).where(Categories.user_id == uid))
        all_cates = categories.scalars().all()
        return all_cates
    except (AttributeError, TypeError, ValueError) as e:
        raise HTTPException(status_code=500, detail=str(e))

async def create_category(category: CreateCategory, db: AsyncSession, uid: int):
    try:
        query = await db.execute(select(Categories).where(Categories.name == category.name, Categories.type == category.type))
        ex_category = query.scalar_one_or_none()

        if ex_category:
            raise HTTPException(status_code=400, detail="A category with the same name and type already exists.")
        
        add_category = Categories(
            user_id = uid,
            name = category.name,
            type = category.type,
        )

        db.add(add_category)
        await db.commit()
        await db.refresh(add_category)
        
        return add_category
    except (SQLAlchemyError) as e:
        raise HTTPException(status_code=500, detail=str(e))


"""
async def edit_category(category: CategoryInfo, category_id: int, db: AsyncSession, uid: int):
    try:
        query = await db.execute(select(Categories).where(Categories.user_id == uid, Categories.id == category_id))
        ex_category = query.scalar_one_or_none()

        if not ex_category:
            raise HTTPException(status_code=404, detail="there is no catogory with this uid")
        
        if ex_category:
            tQuery = await db.execute(select(Transactions).where(Transactions.category_id == ex_category.id))
            trans = tQuery.scalars().all()

            for tran in trans:
                tran.type = ex_category.type

        updated_data = category.model_dump(exclude_unset=True)
        for key, value in updated_data.items():
            setattr(ex_category, key, value)
            
        ex_category.user_id = uid
        ex_category.created_at = datetime.now(timezone.utc)
        
        await db.commit()
        await db.refresh(ex_category)

        return ex_category
    # except:pass
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(status_code=500, detail=f"Exception {str(e)}")
"""

"""
The category will be deleted only if it has no associated transactions. 
Deleting a category with associated transactions requires user confirmation.
"""
async def remove_category(category_id: int, db: AsyncSession, uid: int, force: bool):
    try:       
        query = await db.execute(select(Categories).where(Categories.user_id == uid, Categories.id == category_id))
        ex_category = query.scalar_one_or_none()

        if not ex_category:
            raise HTTPException(status_code=400, detail="There is no category to delete.")
        
        t_query = await db.execute(select(func.count()).select_from(Transactions).where(Transactions.user_id == uid, Transactions.category_id == ex_category.id))
        ex_transactions = t_query.scalar()

        if ex_transactions > 0 and not force:
            raise HTTPException(status_code=409, detail={
                    "message": f"Category contains {ex_transactions} transactions.",
                    "requires_confirmation": True
                }
            )

        if ex_transactions > 0 and force:
            await db.execute(delete(Transactions).where(Transactions.user_id == uid, Transactions.category_id == category_id))
        
        await db.delete(ex_category)
        await db.commit()

        return ex_category
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))