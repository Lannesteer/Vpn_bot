from sqlalchemy import Float, BIGINT
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.base_model import Base
from src.database.keys.models import Key


class User(Base):
    __tablename__ = 'user'

    telegram_id: Mapped[int] = mapped_column(BIGINT, nullable=False)
    balance: Mapped[float] = mapped_column(Float(asdecimal=True), default=0, nullable=True)

    keys: Mapped["Key"] = relationship(
        'Key',
        back_populates='user',
        cascade="all, delete-orphan"
    )