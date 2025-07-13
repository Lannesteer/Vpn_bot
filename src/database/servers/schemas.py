from pydantic import BaseModel, ConfigDict


class ServerCreate(BaseModel):
    type: str
    country: str
    price: int

    model_config = ConfigDict(from_attributes=True)
