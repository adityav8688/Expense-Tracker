from fastapi import FastAPI
from app.database import Base, engine
from app.routers.auth_router import auth_router
from app.routers.category_router import category_router
from app.routers.wallet_router import wallet_router
from app.routers.transaction_router import transaction_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(category_router)
app.include_router(wallet_router)
app.include_router(transaction_router)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "it's working."}