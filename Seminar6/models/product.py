from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int
    title: str = Field(..., title="Title", max_length=100)
    description: str = Field(default='', title="Description", max_length=300)
    price: float = Field(..., title="Price", gt=0, le=1_000_000)


class ProductIn(BaseModel):
    title: str = Field(..., title="Title", max_length=100)
    description: str = Field(default='', title="Description", max_length=300)
    price: float = Field(..., title="Price", gt=0, le=1_000_000)