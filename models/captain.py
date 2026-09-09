from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.user import User


from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.vehicles import Vehicle

class Captain(User):
    __tablename__ = "captains"

    vehicles : Mapped[list["Vehicle"]] = relationship(back_populates="captain")
    