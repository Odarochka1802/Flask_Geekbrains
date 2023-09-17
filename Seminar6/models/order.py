import datetime
from enum import Enum
from pydantic import BaseModel, Field, EmailStr


class Status(Enum):
    unpaid = 'Ждёт оплаты'
    paid = 'Оплачен'
    shipped = 'Отгружен'
    cancelled = 'Отменён'
    completed = 'Выполнен'


class Order(BaseModel):
    order_id: int
    order_date: datetime.date
    order_status: Status
    user_id: int
    user_first_name: str
    user_last_name: str
    user_email: EmailStr
    product_id: int
    product_title: str
    product_description: str
    product_price: float

    class Config:
        use_enum_values = True


class OrderIn(BaseModel):
    user_id: int = Field(..., title="User ID")
    product_id: int = Field(..., title="Product ID")
    date: datetime.date = Field(..., title="Date")
    status: Status = Field(..., title="Status")

    class Config:
        use_enum_values = True
