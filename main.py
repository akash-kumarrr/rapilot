from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from core.config import settings

from core.database import engine
from models.base import Base

from api.auth import router as auth_router
from api.user import router as user_router
from api.book_ride import router as book_ride_route

@asynccontextmanager
async def lifespan(app : FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title=settings.title,
    version=settings.version,
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows any website/domain to connect
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all request headers
)

@app.get("/")
async def root():
    return {
        "service" : "rapilot",
        "status" : "online"
    }

app.include_router(auth_router)
app.include_router(book_ride_route)
app.include_router(user_router)