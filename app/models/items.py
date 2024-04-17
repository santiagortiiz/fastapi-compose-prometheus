from pydantic import BaseModel, Field


class Item(BaseModel):
    name: str
    stock: int
    is_active: bool = True
    price: float | None = Field(default=None, examples=[3.2])


class Message(BaseModel):
    message: str
