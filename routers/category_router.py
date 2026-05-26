from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from core.security import require_role
from models.categories_model import Categories
from schemas.category_schema import CategoryInfo, CreateCategory
from services.category_services import *

category_router = APIRouter(prefix="/category")

@category_router.get("/", response_model=list[CategoryInfo])
def category_list(db: Session = Depends(get_db), role = Depends(require_role("user"))):
    return fetch_categories(db, int(role["user_id"]))

@category_router.post("/")
def add_category(category: CreateCategory, db: Session = Depends(get_db), role = Depends(require_role("user"))):
    return create_category(category, db, int(role["user_id"]))

@category_router.put("/{id}")
def put_category(category: CreateCategory, category_id = id, db: Session = Depends(get_db), role = Depends(require_role("user"))):
    return edit_category(category, category_id, db, int(role["user_id"]))

@category_router.delete("/{id}")
def delete_category(category_id = id, db: Session = Depends(get_db), role = Depends(require_role("user"))):
    return remove_category(category_id, db, int(role["user_id"]))