import datetime
from random import randint, choice
from fastapi import APIRouter
from Seminar6.d_b import orders, products, users, database

router = APIRouter()


@router.get("/data/")
async def create_fake_users(user_cnt: int, prod_cnt: int, order_cnt: int):
    for _ in range(user_cnt):
        user_num = randint(100, 999)
        query = users.insert().values(first_name=f'Name_{user_num}',
                                      last_name=f'LastName_{user_num}',
                                      email=f'user{user_num}@mail.ru',
                                      password=f'pass{randint(1000, 9999)}')
        await database.execute(query)

    for _ in range(prod_cnt):
        prod_num = randint(100, 999)
        query = products.insert().values(title=f'item{prod_num}',
                                         description=f'description{prod_num}',
                                         price=randint(1000, 9999) / 100)
        await database.execute(query)

    for _ in range(order_cnt):
        query = orders.insert().values(user_id=randint(1, user_cnt),
                                       product_id=randint(1, prod_cnt),
                                       date=datetime.date.today(),
                                       status=choice(['Ждёт оплаты', 'Оплачен', 'Отгружен', 'Отменён', 'Выполнен']))
        await database.execute(query)

    return {'message': f'{user_cnt} users, {prod_cnt} products and {order_cnt} orders were created'}
