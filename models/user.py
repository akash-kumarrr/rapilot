from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from models.base import Base

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from models.ride import Ride


class User(Base):
    __tablename__= "users"
    name : Mapped[str] = mapped_column(String)
    email : Mapped[str] = mapped_column(String)
    password : Mapped[str] = mapped_column(String)

    rides : Mapped[List["Ride"]] = relationship(back_populates="passenger")