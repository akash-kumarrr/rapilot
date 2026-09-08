from schemas.ride import RideCreate, RideBase, RideResponse
from models.ride import Ride
from models.user import User

from fastapi import Depends

from sqlalchemy.orm import Session
from sqlalchemy import select


def create_ride(ride_payload : RideCreate, current_user : User, db : Session) :
    ride_payload.user_id = current_user.id
    db_ride = Ride(**ride_payload.model_dump())
    db.add(db_ride)
    db.commit()
    db.refresh(db_ride)
    return db_ride

def read_ride(ride_id : str, db : Session) :
    stmt = select(Ride).where(Ride.id == ride_id)
    data = db.scalars(stmt).first()
    return data

def delete_ride(ride_id : str, db : Session):
    db.delete(select(Ride).where(Ride.id == ride_id))
    return {
        "message" : "data deleted"
    }
