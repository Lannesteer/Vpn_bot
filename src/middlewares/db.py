from aiogram import BaseMiddleware

from database.session import AsyncDatabase


class SessionMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        async with AsyncDatabase.get_session_maker()() as session:
            data["session"] = session
            return await handler(event, data)
