from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.config import settings

from api.auth import router as auth_router

@asynccontextmanager
async def lifespan(app : FastAPI):
    yield

app = FastAPI(
    title=settings.title,
    version=settings.version,
    lifespan=lifespan
)

@app.get("/")
async def root():
    return {
        "service" : "rapilot",
        "status" : "online"
    }

app.include_router(auth_router)