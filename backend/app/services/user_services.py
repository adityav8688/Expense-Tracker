from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime, timezone

from app.models.users_model import Users
from app.utils.hashing import hash_password, verify_pass
from app.core.security import create_access_token

async def create_user(user, db: AsyncSession):
    query = await db.execute(select(Users).where(Users.email == user.email)) #db.query(Users).filter(Users.email == user.email).first()

    ex_user = query.scalar_one_or_none()
    if ex_user:
        raise HTTPException(status_code=400, detail=f"{user.email} is already a registered user.")
    
    user_info = Users(
        name = user.name,
        email = user.email,
        password = hash_password(user.password)
    )

    db.add(user_info)
    await db.commit()
    await db.refresh(user_info)

    return {"message": f"{user.email} is created."}

async def authenticate_user(username, password, db: AsyncSession):
    query = await db.execute(select(Users).where(Users.email == username)) #db.query(Users).filter(Users.email == username).first()

    ex_user = query.scalar_one_or_none()

    if not ex_user:
        raise HTTPException(status_code=404, detail="User not found")
    elif not verify_pass(password, ex_user.password):
        raise HTTPException(status_code=401, detail="incorrect username or password")
    
    ex_user.logged_on = datetime.now(timezone.utc)
    await db.commit()
    await db.refresh(ex_user)

    token = await create_access_token({
        "sub": str(ex_user.id),
        "role": ex_user.role
    })

    return token