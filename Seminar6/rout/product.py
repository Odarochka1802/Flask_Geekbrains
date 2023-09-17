from fastapi import APIRouter, HTTPException
from Seminar6.d_b import products, database
from Seminar6.models.product import Product, ProductIn

router = APIRouter()


@router.get("/products/", response_model=list[Product])
async def get_products():
    query = products.select()
    return await database.fetch_all(query)


@router.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    fetch = await database.fetch_one(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='Product not found')
    return fetch


@router.post("/products/", response_model=Product)
async def add_product(product: ProductIn):
    query = products.insert().values(title=product.title,
                                     description=product.description,
                                     price=product.price)
    last_record_id = await database.execute(query)
    return {**product.model_dump(), "id": last_record_id}


@router.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, new_product: ProductIn):
    query = products.update().where(products.c.id == product_id).values(**new_product.model_dump())
    fetch = await database.execute(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='Product not found')
    return {**new_product.model_dump(), "id": product_id}


@router.delete("/products/{product_id}")
async def delete_product(product_id: int):
    query = products.delete().where(products.c.id == product_id)
    fetch = await database.execute(query)
    if not fetch:
        raise HTTPException(status_code=404, detail='Product not found')
    return {'message': 'Product deleted'}