from sqlalchemy import select
from sqlalchemy.orm import selectinload

from database.session import session_handler
from src.database.base_class import BaseService
from src.database.keys.models import Key


class KeyService(BaseService[Key]):
    def __init__(self):
        super().__init__(Key)

    @session_handler
    async def get_key(self, session, key_id):
        stmt = select(self.model).where(self.model.id == key_id).options(
            selectinload(self.model.server)
        )
        result = await session.execute(stmt)
        key = result.scalar_one_or_none()
        return key


key_service = KeyService()
