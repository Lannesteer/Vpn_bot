import uuid

from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base_model import Base


class Server(Base):
    __tablename__ = 'server'

    type: Mapped[str] = mapped_column(nullable=False)
    country: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[uuid.UUID] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)

    key = relationship(back_populates="key", cascade="all, delete-orphan")
