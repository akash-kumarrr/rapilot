from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.captain import Captain
    
from models.base import Base

class Vehicle(Base) :
    __tablename__ = "vehicles"

    vehicle : Mapped[str] = Mapped(String)
    category : Mapped[str] = Mapped(String)
    vehicle_number : Mapped[str] = Mapped(String)

    captain_id : Mapped[str] = Mapped(ForeignKey("captains.id"))
    captain : Mapped["Captain"] = relationship(back_populates="vehicles")