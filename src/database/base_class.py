from datetime import datetime
from typing import TypeVar, Type, Generic

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from src.database.base_model import Base
from src.database.session import session_handler

ModelType = TypeVar('ModelType', bound=Base)


class BaseService(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    @session_handler
    async def all(self, session):
        result = await session.scalars(select(self.model))
        if not result:
            return []
        return result.all()

    async def id(self, session, model_id: str) -> object:
        model = await session.get(self.model, model_id)
        if model is not None:
            return model

    @session_handler
    async def create(self, session, data):
        try:
            model = self.model(**data.dict())
            session.add(model)
            await session.commit()
            await session.refresh(model)
            return model
        except IntegrityError as error:
            pass

    @session_handler
    async def delete(self, session, model_id: str):
        model = await self.id(session, model_id)
        await session.delete(model)
        await session.commit()
        return 200

    @session_handler
    async def update(self, session, model_id: str, update_data):
        model = await self.id(session, model_id)
        update_data = update_data.dict(exclude_unset=True)
        for key, value in update_data.items():
            if value is not None:
                setattr(model, key, value)
        model.updated_at = datetime.utcnow()
        await session.commit()
        return model
