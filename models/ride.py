from sqlalchemy import String, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING

from models.base import Base

if TYPE_CHECKING:
    from models.user import User

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