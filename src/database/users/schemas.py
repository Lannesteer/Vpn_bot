from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):
    tg_user_id: str

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    balance: float

    model_config = ConfigDict(from_attributes=True)
