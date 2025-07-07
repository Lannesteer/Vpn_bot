from typing import List

from sqlalchemy import Float
from sqlalchemy.orm import mapped_column, Mapped, relationship

from database.base_model import Base


class User(Base):
    __tablename__ = 'user'
    telegram_id: Mapped[str] = mapped_column(nullable=False)
    balance: Mapped[float] = mapped_column(Float(asdecimal=True), nullable=True)

    keys: Mapped[List["Key"]] = relationship(back_populates="user", cascade="all, delete-orphan")
