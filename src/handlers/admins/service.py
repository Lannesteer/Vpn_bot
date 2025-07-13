from src.database.servers.schemas import ServerCreate
from src.database.servers.service import server_service


class AdminService:
    async def add_server(self, data):
        result = await server_service.create(
            ServerCreate(
                type=data.get("type"),
                country=data.get("country"),
                price=data.get("price")
            )
        )
        return result


admin_service = AdminService()
