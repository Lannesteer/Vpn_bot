from sqlalchemy import select

from src.database.session import session_handler
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

    @session_handler
    async def get_server_by_country(self, session, country: str):
        result = await session.execute(
            select(self.model)
            .where(self.model.country == country)
        )
        server = result.scalars().one()
        return server


server_service = ServerService()
