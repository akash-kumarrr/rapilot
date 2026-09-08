from pydantic import BaseModel, computed_field
from services.geoalgo import geohashing
from enum import Enum

class RideOption(str, Enum):
    BIKE = "Bike"
    CAB_ECONOMY = "Cab-Economy"
    CAB_PREMIUM = "Cab-Premium"

class RideBase(BaseModel):
    starting_point_longitude : float
    starting_point_latitude : float
    destination_point_longitude : float
    destination_point_latitude : float
    ride_option : RideOption

    @computed_field
    @property
    def starting_point_geohash(self) -> str:
        return geohashing(longitude=self.starting_point_longitude, latitude=self.starting_point_latitude)

    @computed_field
    @property
    def destination_point_geohash(self) -> str:
        return geohashing(longitude=self.destination_point_longitude, latitude=self.destination_point_latitude)
    

class RideCreate(RideBase):
    user_id: str

class RideResponse(RideCreate):
    id: str

    class Config:
        from_attributes = True    