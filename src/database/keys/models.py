import uuid
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.base_model import Base


class Key(Base):
    __tablename__ = 'key'

    access_url: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    server_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("server.id", ondelete="CASCADE"), nullable=False)
    status: Mapped[bool] = mapped_column(default=True)
    expiry_date: Mapped[datetime] = mapped_column(default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="keys")
    server = relationship("Server", back_populates="keys")
