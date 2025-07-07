from functools import wraps

from sqlalchemy import exc, text
from sqlalchemy.exc import DBAPIError

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from ssl import create_default_context, Purpose as SSLPurpose
import sqlalchemy.engine.url as SQURL
from src.config import DbConfig


class AsyncDatabaseSessions:
    def __init__(self):
        self.URL = SQURL.URL.create(
            drivername="postgresql+asyncpg",
            username=DbConfig.user,
            password=DbConfig.password,
            host=DbConfig.host,
            port=DbConfig.port,
            database=DbConfig.name,
        )
        if DbConfig.ssl != "None":
            self.ctx = create_default_context(
                SSLPurpose.SERVER_AUTH,
                cafile=DbConfig.ssl
            )
            self.ctx.check_hostname = True

            self.engine = create_async_engine(self.URL, pool_size=50, max_overflow=-1, connect_args={"ssl": self.ctx})
        else:
            self.engine = create_async_engine(self.URL, pool_size=50, max_overflow=-1)
        self.factory = async_sessionmaker(self.engine, class_=AsyncSession, expire_on_commit=False)

    def get_url(self):
        return str(self.URL)

    def get_session_maker(self) -> async_sessionmaker:
        return self.factory

    async def get_session(self) -> AsyncSession:
        async with self.factory() as session:
            try:
                yield session
            except exc.SQLAlchemyError as error:
                await session.rollback()
                raise

    async def return_session(self) -> AsyncSession:
        return self.factory()


AsyncDatabase = AsyncDatabaseSessions()


async def main():
    session = await AsyncDatabase.return_session()
    await session.execute(text("SELECT * FROM users"))


def session_handler(func):
    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        if "session" in kwargs:
            session = kwargs["session"]
        else:
            session: AsyncSession = await AsyncDatabase.return_session()
        try:
            result = await func(self, session, *args, **kwargs)
        except DBAPIError as e:
            result = await func(self, session, *args, **kwargs)
        finally:
            if "session" not in kwargs:
                await session.close()
        return result

    return wrapper
