from jose import jwt, JWTError
from jose.exceptions import ExpiredSignatureError
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings
from datetime import datetime, timezone, timedelta

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

#creates token for user
async def create_access_token(data: dict):
    encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(hours=2)
    encode.update({"exp":expire})
    return jwt.encode(encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

#used for user authorization
async def get_current_user(
        token: str = Depends(oauth2_scheme)
    ):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)

    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="token expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="invalid token")
    
    user_id = payload.get("sub")
    user_role = payload.get("role")
    return {
        "user_id" : user_id,
        "role" : user_role
    }

#used for role authorization
def require_role(req_role: str):
    
    def role_checker(current_user = Depends(get_current_user)):
        if current_user["role"] != req_role:
            raise HTTPException(status_code=403, detail="Access denied")
        
        return current_user
    return role_checker