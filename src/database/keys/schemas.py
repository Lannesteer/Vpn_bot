from datetime import date

from pydantic import BaseModel, ConfigDict


class KeyCreate(BaseModel):
    id: int
    access_url: str
    user_id: int
    expiry_date: date

    model_config = ConfigDict(from_attributes=True)


class KeyUpdate(BaseModel):
    expiry_date: date

    model_config = ConfigDict(from_attributes=True)
