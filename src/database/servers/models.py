from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base_model import Base


class Server(Base):
    __tablename__ = 'server'

    type: Mapped[str] = mapped_column(nullable=False)
    country: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)

    keys = relationship(
        'Key',
        back_populates="server",
        cascade="all, delete-orphan"
    )