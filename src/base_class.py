from typing import TypeVar, Type, Generic

from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import Base

ModelType = TypeVar('ModelType', bound=Base)


class BaseService(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], session: AsyncSession):
        self.table = model
        self.session = session

    async def get_one(self, item_id: int | str):
        if isinstance(item_id, int):
            item = await self.session.execute(
                select(self.table).filter_by(id=item_id)
            )
        else:
            item = await self.session.execute(
                select(self.table).filter_by(tg_user_id=item_id)
            )

        db_item = item.scalar()

        return db_item

    async def get_list(self, filters: int):
        query = await self.session.execute(
            select(self.table).limit(filters).order_by(-self.table.id.desc())
        )
        return query.scalars().all()

    async def create(self, data):
        item = self.table(**data.dict())
        self.session.add(item)
        await self.session.commit()
        return item

    async def update(self, data, item_id: int | str):
        if isinstance(item_id, int):
            await self.session.execute(update(self.table).filter_by(id=item_id), data.dict())
        else:
            await self.session.execute(update(self.table).filter_by(tg_user_id=item_id), data.dict())
        await self.session.commit()
        return {'response': 'updated'}

    async def delete(self, item_id: int):
        await self.session.execute(delete(self.table).filter_by(id=item_id))
        await self.session.commit()
        return {'response': 'deleted'}
