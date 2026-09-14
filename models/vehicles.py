from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.ride import Ride
    from models.captain import Captain

class Vehicle(Base):
    __tablename__ = "vehicles"
    vehicle_type : Mapped[str] = mapped_column(String)
    vehicle_number : Mapped[str] = mapped_column(String)

    captain_id : Mapped[str] = mapped_column(ForeignKey("captains.id"))
    captain : Mapped["Captain"] = relationship(back_populates="vehicles")

    rides_given : Mapped["Ride"] = relationship(back_populates="vechicle_used")