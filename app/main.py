from fastapi import FastAPI
import uvicorn

from core.db import SessionLocal, Base, engine
from routers.routers import api_router

app = FastAPI()

Base.metadata.create_all(engine)
app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app",
                host="localhost",
                reload=True)