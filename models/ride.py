from sqlalchemy import String, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING

from models.base import Base

if TYPE_CHECKING:
    from models.user import User
    from models.captain import Captain
    from models.vehicles import Vehicle

class Ride(Base):
    __tablename__ = "rides_booked"
    starting_point_longitude : Mapped[float] = mapped_column(Float)
    starting_point_latitude : Mapped[float] = mapped_column(Float)
    destination_point_longitude : Mapped[float] = mapped_column(Float)
    destination_point_latitude : Mapped[float] = mapped_column(Float)
    starting_point_geohash : Mapped[str] = mapped_column(String)
    destination_point_geohash : Mapped[str] = mapped_column(String)

    user_id : Mapped[str] = mapped_column(ForeignKey("users.id"))
    passenger : Mapped["User"] = relationship(back_populates="rides")

    captian_id : Mapped[str] = mapped_column(ForeignKey("captains.id"))
    captian : Mapped["Captain"] = relationship(back_populates="ride_as_captain")

    vehicle_id : Mapped[str] = mapped_column(ForeignKey("vechicles.id"))
    vehicle : Mapped["Vehicle"] = relationship(back_populates="vehicle")