from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.user import User


from core.security import get_current_user, get_db

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.get("/rides-booked")
async def get_rides_booked(current_user : User = Depends(get_current_user), db : Session = Depends(get_db)):
    return current_user.rides