from pydantic import BaseModel, computed_field
from services.geoalgo import geohashing

class DriverBase(BaseModel):
    name : str 

class DriverLiveLoation(DriverBase):
    longitude : float
    latitude : float

    @property
    @computed_field
    def live_geo_hash(self) -> str :
        return geohashing(
            longitude=self.longitude,
            latitude=self.latitude
        )