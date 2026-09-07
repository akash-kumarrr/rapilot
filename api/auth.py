from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from schemas.user import UserBase, UserResponse, UserCreate

from models.user import User

from sqlalchemy.orm import Session
from sqlalchemy import select

from core.config import settings
from core.database import get_db
from core.security import verify_password, create_access_token, get_current_user

from deps.user import create, delete, read

from services.exceptions import *


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(new_user_payload : UserCreate, db : Session =  Depends(get_db)):
    try:
        return create(new_user_payload, db=db)
    except HTTPException : 
        raise
    except Exception as e :
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.post("/login", status_code=status.HTTP_200_OK)
async def login(credentials : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    stmt = select(User).where(User.email == credentials.username)
    user = db.execute(stmt).scalar_one_or_none()

    if not user or not verify_password(credentials.password, User.password):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Invalid email or password",
            headers={"WWW-Authentication" : "Bearer"}
        )

    access_token = create_access_token(str(user.id))

    return {
        "access_token" : access_token,
        "token_type" : "bearer"
    }

@router.get("/me")
async def read_user_me(current_user : User = Depends(get_current_user)):
    return current_user

