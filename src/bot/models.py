from typing import Annotated, List

from sqlalchemy import Float, DateTime, func, ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

date = Annotated[DateTime, mapped_column(DateTime, default=func.now())]


class Key(Base):
    __tablename__ = 'key'

    id: Mapped[int] = mapped_column(primary_key=True)
    access_url: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[str] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    activation_date: Mapped[date]
    expiry_date: Mapped[date]
    status: Mapped[bool] = mapped_column(default=True)

    user: Mapped["User"] = relationship(back_populates="keys")


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_user_id: Mapped[str] = mapped_column(nullable=False)
    balance: Mapped[float] = mapped_column(Float(asdecimal=True), nullable=True)

    keys: Mapped[List["Key"]] = relationship(back_populates="user", cascade="all, delete-orphan")
