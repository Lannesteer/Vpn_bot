from sqlalchemy import select

from database.session import session_handler
from src.database.base_class import BaseService
from src.database.servers.models import Server


class ServerService(BaseService[Server]):
    def __init__(self):
        super().__init__(Server)

    @session_handler
    async def get_servers_by_country(self, session, country: str):
        result = await session.execute(
            select(self.model)
            .where(
                self.model.country.ilike(f'%{country}%')
            )
        )
        servers = result.scalars().all()
        return servers


server_service = ServerService()
