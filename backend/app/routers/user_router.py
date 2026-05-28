from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from typing import Annotated

from app.models.users_model import Users
from app.schemas.user_schema import UserCreate, UserInfo
from app.core.database import get_db
from app.services.user_services import create_user, authenticate_user
from app.core.security import require_role

user_router = APIRouter()


@user_router.post("/register")
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        return await create_user(user, db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@user_router.post("/login")
async def login_user(user: Annotated[OAuth2PasswordRequestForm, Depends()], db: AsyncSession = Depends(get_db)):
    try:
        token = await authenticate_user(user.username, user.password, db)

        return {
            "access_token": token,
            "token_type": "bearer"
            }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@user_router.get("/admin", response_model=list[UserInfo])
async def admin_dashboard(db: AsyncSession=Depends(get_db),curren_user = Depends(require_role("admin"))):
    try:
        users = db.query(Users).all()
        return users
    except Exception as e:
        print(str(e))