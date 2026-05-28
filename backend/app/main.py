from fastapi import FastAPI
from app.core.database import Base, engine
from app.routers.user_router import user_router
from app.routers.category_router import category_router
from app.routers.wallet_router import wallet_router
from app.routers.transaction_router import transaction_router

app = FastAPI()

app.include_router(user_router)
app.include_router(category_router)
app.include_router(wallet_router)
app.include_router(transaction_router)

@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def root():
    return {"message": "it's working."}