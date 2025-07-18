import asyncio
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from celery import current_task
from sqlalchemy.ext.asyncio import async_scoped_session, AsyncSession

from src.database.session import AsyncDatabase

loop = asyncio.get_event_loop()

session_factory = AsyncDatabase.get_session_maker()


@asynccontextmanager
async def scoped_session() -> AsyncGenerator[AsyncSession, None]:
    scoped_factory = async_scoped_session(
        session_factory,
        scopefunc=current_task,
    )
    try:
        async with scoped_factory() as session:
            yield session
    finally:
        await scoped_factory.remove()
