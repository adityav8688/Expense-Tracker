from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from models.users_model import Users
from utils.hashing import hash_password, verify_pass
from core.security import create_access_token

def create_user(user, db: Session):
    ex_user = db.query(Users).filter(Users.email == user.email).first()

    if ex_user:
        raise HTTPException(status_code=400, detail="User already there with this email")
    
    user_info = Users(
        name = user.name,
        email = user.email,
        password = hash_password(user.password)
    )

    db.add(user_info)
    db.commit()
    db.refresh(user_info)

def authenticate_user(username, password, db: Session):
    ex_user = db.query(Users).filter(Users.email == username).first()

    if not ex_user:
        raise HTTPException(status_code=404, detail="User not found")
    elif not verify_pass(password, ex_user.password):
        raise HTTPException(status_code=401, detail="incorrect username or password")
    
    ex_user.logged_on = datetime.now()
    db.commit()
    db.refresh(ex_user)

    token = create_access_token({
        "sub": str(ex_user.id),
        "role": ex_user.role
    })

    return token