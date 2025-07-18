from src.celery_worker.session import loop, scoped_session
from src.database.keys.service import key_service
from src.database.users.service import user_service
from src.handlers.users.vpn.utils import vpn_utils
from src.database.users.schemas import UserUpdate
from src.celery_worker.celery_worker import celery_app


@celery_app.task
def check_balance(telegram_id, key_id):
    return loop.run_until_complete(check_balance_async(telegram_id, key_id))


async def check_balance_async(telegram_id, key_id):
    async with scoped_session() as session:
        user = await user_service.get_user_by_telegram_id(session, telegram_id)
        key = await key_service.get_key(session, key_id)

        if user.balance < 200:
            await key_service.delete(session, key.id)
            await vpn_utils.notify_users(
                telegram_id=telegram_id,
                text=f'Не удалось списать стоимость ключа с сервера '
                     f'{key.server.country}, 100GB, {key.server.price}₽/месяц  '
                     f'сумме {key.server.price}. Ключ удален',
            )
        else:
            data = UserUpdate(balance=user.balance - 200)
            await user_service.update(session, data, user.id)
