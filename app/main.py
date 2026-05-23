from fastapi import FastAPI
from app.database import Base, engine
from routers.auth import auth_router

app = FastAPI()

app.include_router(auth_router)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "it's working."}