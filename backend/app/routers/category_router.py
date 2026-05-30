from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.core.database import get_db
from app.core.security import require_role
from app.schemas.category_schema import CategoryInfo, CreateCategory
from app.services.category_services import *

category_router = APIRouter(prefix="/category")

@category_router.get("/", response_model=list[CategoryInfo])
async def category_list(db: Session = Depends(get_db), role = Depends(require_role("user"))):
    return await fetch_categories(db, int(role["user_id"]))

@category_router.post("/")
async def add_category(category: CreateCategory, db: Session = Depends(get_db), role = Depends(require_role("user"))):
    return await create_category(category, db, int(role["user_id"]))


@category_router.patch("/{id}")
async def put_category(category: CategoryInfo, id: int, db: Session = Depends(get_db), role = Depends(require_role("user"))):
    return await edit_category(category, id, db, int(role["user_id"]))

@category_router.delete("/{id}")
async def delete_category(id: int, db: Session = Depends(get_db), role = Depends(require_role("user"))):
    return await remove_category(id, db, int(role["user_id"]))
