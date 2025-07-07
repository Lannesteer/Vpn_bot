import logging

from select import select

from database.base_class import BaseService
from database.session import session_handler
from database.users.models import User


class UserService(BaseService[User]):
    def __init__(self):
        super().__init__(User)

    @session_handler
    async def get_user_by_telegram_id(self, session, telegram_id: int):
        try:
            user = await session.execute(
                select(self.model).filter_by(telegram_id=telegram_id)
            )
            user = user.scalar()
            return user
        except Exception as e:
            logging.error(e)
            return None


user_service = UserService()
