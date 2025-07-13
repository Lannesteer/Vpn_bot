from src.database.base_class import BaseService
from src.database.servers.models import Server


class ServerService(BaseService[Server]):
    def __init__(self):
        super().__init__(Server)


server_service = ServerService()
