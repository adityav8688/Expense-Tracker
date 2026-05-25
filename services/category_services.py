from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from models.categories_model import Categories
from schemas.category_schema import CreateCategory, CategoryInfo

def fetch_categories(db: Session, id:int):
    categories = db.query(Categories).filter(Categories.user_id == id).all()
    
    return categories

def create_category(category: CreateCategory, db: Session, id: int):
    add_category = Categories(
        user_id = id,
        name = category.name,
        type = category.type,
        color = category.color,
        icon = category.icon
    )

    db.add(add_category)
    db.commit()
    db.refresh(add_category)
    
    return {"message" : "Category created."}

def edit_category(category: CategoryInfo, category_id: int, db: Session, id: int):
    ex_category = db.query(Categories).filter(Categories.user_id == id, Categories.id == category_id).first()

    if not ex_category:
        raise HTTPException(status_code=404, detail="there is no catogory with this id")

    ex_category.user_id = id
    ex_category.name = category.name
    ex_category.type = category.type
    ex_category.color = category.color
    ex_category.icon = category.icon
    ex_category.created_at = datetime.now(timezone.utc)
    

    db.commit()
    db.refresh(ex_category)

    return {"message": "Category Updated."}

def remove_category(category_id: int, db: Session, id: int):
    del_category = db.query(Categories).filter(Categories.user_id == id, Categories.id == category_id).first()

    db.delete(del_category)
    db.commit()

    return {"message": "Category Deleted."}