from src.database.base_class import BaseService
from src.database.keys.models import Key


class KeyService(BaseService[Key]):
    def __init__(self):
        super().__init__(Key)


key_service = KeyService()
