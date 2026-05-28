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
    try:
        return await fetch_categories(db, int(role["user_id"]))
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

@category_router.post("/")
async def add_category(category: CreateCategory, db: Session = Depends(get_db), role = Depends(require_role("user"))):
    try:
        return await create_category(category, db, int(role["user_id"]))
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

@category_router.put("/{id}")
async def put_category(category: CreateCategory, category_id = id, db: Session = Depends(get_db), role = Depends(require_role("user"))):
    try:
        return await edit_category(category, int(category_id), db, int(role["user_id"]))
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

@category_router.delete("/{id}")
async def delete_category(category_id = id, db: Session = Depends(get_db), role = Depends(require_role("user"))):
    try:
        return await remove_category(int(category_id), db, int(role["user_id"]))
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))