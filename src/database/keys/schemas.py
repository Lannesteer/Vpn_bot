
import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class KeyCreate(BaseModel):
    id: uuid.UUID
    access_url: str
    user_id: uuid.UUID
    server_id: uuid.UUID
    expiry_date: datetime

    model_config = ConfigDict(from_attributes=True)


class KeyUpdate(BaseModel):
    expiry_date: datetime

    model_config = ConfigDict(from_attributes=True)
