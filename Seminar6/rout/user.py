from fastapi import APIRouter, HTTPException

from Seminar6.d_b import users, database
from Seminar6.models.user import User, UserIn

router = APIRouter()


@router.get("/users/", response_model=list[User])
async def get_users():
    query = users.select()
    return await database.fetch_all(query)


@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    fetch = await database.fetch_one(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='User not found')
    return fetch


@router.post("/users/", response_model=User)
async def add_user(user: UserIn):
    query = users.insert().values(first_name=user.first_name,
                                  last_name=user.last_name,
                                  email=user.email,
                                  password=user.password)
    last_record_id = await database.execute(query)
    return {**user.model_dump(), "id": last_record_id}


@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.model_dump())
    fetch = await database.execute(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='User not found')
    return {**new_user.model_dump(), "id": user_id}


@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    fetch = await database.execute(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='User not found')
    return {'message': 'User deleted'}