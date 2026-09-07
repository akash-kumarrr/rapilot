from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from models.base import Base


class User(Base):
    name : Mapped[str] = mapped_column(String)
    email : Mapped[str] = mapped_column(String)
    password : Mapped[str] = mapped_column(String)