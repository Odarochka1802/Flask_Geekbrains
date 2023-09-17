from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    id: int
    first_name: str = Field(..., title="First Name", max_length=60)
    last_name: str = Field(..., title="Last Name", max_length=60)
    email: EmailStr = Field(..., title="Email", max_length=120)


class UserIn(BaseModel):
    first_name: str = Field(..., title="First Name", max_length=60)
    last_name: str = Field(..., title="Last Name", max_length=60)
    email: EmailStr = Field(..., title="Email", max_length=80)
    password: str = Field(..., title="Password", min_length=6, max_length=20)