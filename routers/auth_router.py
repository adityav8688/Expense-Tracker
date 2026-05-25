from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import Annotated

from models.users_model import Users
from schemas.user_schema import UserCreate, UserInfo
from app.database import get_db
from services.auth_services import create_user, authenticate_user
from core.security import require_role

auth_router = APIRouter()


@auth_router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    
    create_user(user, db)

    return {"message":"user created"}

@auth_router.post("/login")
def login_user(user: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
    token = authenticate_user(user.username, user.password, db)

    return {
        "access_token":token,
        "token_type":"bearer"
        }

@auth_router.get("/admin", response_model=list[UserInfo])
def admin_dashboard(db: Session=Depends(get_db),curren_user = Depends(require_role("admin"))):
    users = db.query(Users).all()

    return users
    