from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.user import Base


from typing import TYPE_CHECKING

if TYPE_CHECKING: 
    from models.vehicles import Vehicle
    from models.ride import Ride


class Captain(Base):
    __tablename__ = "captains"

    vehicles : Mapped[list["Vehicle"]] = relationship(back_populates="captain")

    rides_drived : Mapped[list["Ride"]] = relationship(back_populates="captain")