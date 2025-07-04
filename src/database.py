from typing import AsyncGenerator

from sqlalchemy import exc
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
# from redis import asyncio as aioredis

from src.config import DBConfig, RedisConfig
from src.config import dbconfig, redis_config


class Base(DeclarativeBase):
    pass


class DBManager:
    def __init__(self, db_config: DBConfig, redis_config: RedisConfig):
        self.database_url = f"postgresql+asyncpg://{db_config.user}:{db_config.password}@{db_config.host}:{db_config.port}/{db_config.name}"
        # self.redis = aioredis.from_url(f"redis://{redis_config.host}:{redis_config.port}")
        self.engine = create_async_engine(self.database_url)
        self.async_session_maker = async_sessionmaker(self.engine, expire_on_commit=False)

    async def get_async_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.async_session_maker() as session:
            try:
                yield session
            except exc.SQLAlchemyError as error:
                await session.rollback()
                raise

    async def get_session(self) -> AsyncSession:
        return self.async_session_maker()


db_manager = DBManager(dbconfig, redis_config)


async def get_async_session():
    return db_manager.get_session()
