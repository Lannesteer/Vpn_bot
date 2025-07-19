import asyncio
import uuid
from datetime import datetime, timedelta

from src.config import CeleryConfig
from src.database.keys.schemas import KeyCreate
from src.database.keys.service import key_service
from src.services.outline.manager import outline_manager
from src.celery_worker.tasks import check_balance


class VpnService:
    async def configurate_vpn_key(self, server, user):
        vpn_client = await outline_manager.vpn_client_init(server)
        key = vpn_client.create_key(
            key_id=str(uuid.uuid4()),
            name=str(user.telegram_id),
            data_limit=107374182400
        )

        task = asyncio.create_task(
            key_service.create(
                KeyCreate(
                    id=uuid.UUID(key.key_id),
                    access_url=key.access_url,
                    user_id=user.id,
                    server_id=server.id,
                    expiry_date=datetime.utcnow() + timedelta(minutes=30)
                )

            )
        )
        check_balance.apply_async(args=[user.telegram_id, key.key_id], countdown=30)

        return f'{key.access_url}&prefix=POST%20'


vpn_service = VpnService()
