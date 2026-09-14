from fastapi import APIRouter, Depends

from core.database import get_db
from core.security import get_current_user
from schemas.ride import RideCreate, RideResponse, RideBase
from sqlalchemy.orm import Session

from models.user import User

from deps.ride import create_ride, read_ride, delete_ride, get_near_rides

router = APIRouter(
    prefix="/ride",
    tags=["ride"]
)

@router.post("/book")
async def book(ride : RideCreate, current_user : User = Depends(get_current_user), db : Session = Depends(get_db)):
    try :
        return create_ride(ride, current_user=current_user, db=db)
    except Exception : 
        raise  

@router.get("/get")
async def get(ride_id : str, db : Session = Depends(get_db)):
    try :
        return read_ride(ride_id=ride_id, db=db)
    except Exception :
        raise

@router.delete("/delete")
async def get(ride_id : str, db : Session = Depends(get_db)):
    try : 
        return delete_ride(ride_id=ride_id, db=db)
    except Exception:
        raise


@router.get("/get-nearby-request")
async def get_nearby_requests(captain_live_long : float, captain_live_lat : float):
    "Ride Requests nearby by captain live location"
    try :
        return get_near_rides(captain_live_long, captain_live_lat)
    except Exception :
        raise
