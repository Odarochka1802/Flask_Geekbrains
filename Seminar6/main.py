import uvicorn
from fastapi import FastAPI
from d_b import database
from rout import user, product, order, data

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(user.router, tags=["users"])
app.include_router(product.router, tags=["products"])
app.include_router(order.router, tags=["orders"])
app.include_router(data.router, tags=["data"])

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )