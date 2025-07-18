import asyncio

from src.database.session import AsyncDatabase

loop = asyncio.get_event_loop()

session_factory = AsyncDatabase.get_session_maker()
