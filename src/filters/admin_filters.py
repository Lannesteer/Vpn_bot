from aiogram.filters import Filter
from aiogram.types import Message

from src.config import BotConfig


class AdminFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        user_id = message.from_user.id
        return user_id in BotConfig.superusers_ids
