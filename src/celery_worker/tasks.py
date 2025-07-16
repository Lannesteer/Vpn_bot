import asyncio

from src.database.keys.service import key_service
from src.database.users.service import user_service
from src.handlers.users.vpn.utils import vpn_utils
from src.database.users.schemas import UserUpdate
from src.celery_worker.celery_worker import celery_app


@celery_app.task
def check_balance(telegram_id, key_id):
    """
    Проверяет баланс пользователя и удаляет ключ, если недостаточно средств.
    """

    async def async_task():
        user = await user_service.get_user_by_telegram_id(telegram_id)
        key = await key_service.id(key_id)
        if user.balance < 200:
            await key_service.delete(key.id)
            await vpn_utils.notify_users(
                telegram_id=telegram_id,
                text=f'Не удалось списать стоимость ключа с сервера '
                     f'{key.server.country}, 100GB, {key.server.price}₽/месяц  '
                     f'сумме {key.server.price}. Ключ удален')
        else:
            data = UserUpdate(balance=user.balance - 200)
            await user_service.update(data, user.id)

    asyncio.run(async_task())
