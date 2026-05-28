from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy import select
from datetime import datetime, timezone
from typing import Annotated

from app.models.categories_model import Categories
from app.schemas.category_schema import CreateCategory, CategoryInfo

async def fetch_categories(db: AsyncSession, uid:int):
    try:
        categories = await db.execute(select(Categories).where(Categories.user_id == uid)) #db.query(Categories).filter(Categories.user_id == uid).all()
        all_cates = categories.scalars().all()
        return all_cates
    except Exception:
        raise HTTPException(status_code=500, detail="Check category_services.py")

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
            color = category.color,
            icon = category.icon
        )

        db.add(add_category)
        await db.commit()
        await db.refresh(add_category)
        
        return category
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    except AttributeError as e:
        raise HTTPException(status_code=422, detail=str(e))

async def edit_category(category: CategoryInfo, category_id: int, db: AsyncSession, uid: int):
    try:
        query = await db.execute(select(Categories).where(Categories.user_id == uid, Categories.uid == category_id)) #db.query(Categories).filter(Categories.user_id == uid, Categories.uid == category_id).first()
        ex_category = query.scalar_one_or_none()

        if not ex_category:
            raise HTTPException(status_code=404, detail="there is no catogory with this uid")

        ex_category.user_id = uid
        ex_category.name = category.name
        ex_category.type = category.type
        ex_category.color = category.color
        ex_category.icon = category.icon
        ex_category.created_at = datetime.now(timezone.utc)
        

        await db.commit()
        await db.refresh(ex_category)

        return ex_category
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

async def remove_category(category_id: int, db: AsyncSession, uid: int):
    try:
            
        query = await db.execute(select(Categories).where(Categories.user_id == uid, Categories.id == category_id)) #db.query(Categories).filter(Categories.user_id == uid, Categories.uid == category_id).first()
        ex_category = query.scalar_one_or_none()

        if not ex_category:
            raise HTTPException(status_code=400, detail="There is no category to delete")
        
        await db.delete(ex_category)
        await db.commit()

        return ex_category
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=str(e))