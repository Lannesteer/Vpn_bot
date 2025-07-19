import asyncio

from src.handlers.users.vpn.text import VpnTexts
from src.services.outline.manager import outline_manager
from src.database.keys.service import key_service
from src.database.users.service import user_service
from src.handlers.users.vpn.utils import vpn_utils
from src.database.users.schemas import UserUpdate
from src.celery_worker.celery_worker import celery_app

# создаем глобальный loop так как Celery не работает с asyncio.run() и async функциями
loop = asyncio.get_event_loop()


@celery_app.task()
def check_balance(telegram_id, key_id):
    return loop.run_until_complete(check_balance_async(telegram_id, key_id))


async def check_balance_async(telegram_id, key_id):
    user = await user_service.get_user_by_telegram_id(telegram_id)
    key = await key_service.get_key(key_id)

    if user.balance < 200:
        await key_service.delete(key.id)
        vpn_client = await outline_manager.vpn_client_init(key.server)
        vpn_client.delete_key(key.id)
        vpn_utils.notify_users_from_celery(
            telegram_id=telegram_id,
            text=VpnTexts.PaymentError.format(
                Server=key.server.country,
                Price=key.server.price)
        )
    else:
        data = UserUpdate(balance=user.balance - 200)
        await user_service.update(data, user.id)
