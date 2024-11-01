# app.py
from fastapi import FastAPI
from .controllers.rest_api import router_customers, router_products

app = FastAPI()

# Include the routers
app.include_router(router_customers.customer_router)
app.include_router(router_products.prod_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the API!"}
