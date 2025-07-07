from aiogram.types import CallbackQuery, Message

from src.database.users.service import user_service


async def UserMiddleware(handler, event, data: dict):
    if isinstance(event, Message):
        user_id = event.from_user.id
    elif isinstance(event, CallbackQuery):
        user_id = event.from_user.id
    else:
        return await handler(event, data)

    user = await user_service.get_user_by_telegram_id(user_id)
    data['user'] = user
    return await handler(event, data)
