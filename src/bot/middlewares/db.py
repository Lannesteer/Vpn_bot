from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, TelegramObject

from bot.handlers.keys.service import get_key_service


class DataBaseSession(BaseMiddleware):
    def __init__(self, session):
        self.session = session

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        data['service'] = await get_key_service(self.session)
        return await handler(event, data)


class UserIDMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: Dict[str, Any]
    ) -> Any:
        data["user_id"] = data["event_from_user"].id

        return await handler(event, data)
