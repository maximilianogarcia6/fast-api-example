# mover todas las funciones de api de app.py aca usando router api
#

from fastapi import APIRouter, HTTPException
from .schemas.customer import Customer

customer_router = APIRouter(
    prefix="/customers",
    tags=["customer"]
    )

customers = []

@customer_router.get("/")
async def get_customers():
    return customers

@customer_router.get("/{id}")
async def get_customer(customer_id: int):
    for customer in customers:
        if customer.id == customer_id:
            return customer
    
    raise HTTPException(status_code=404, detail="Item not found")


@customer_router.post("/")
async def create_item(customer: Customer):
    customers.append(customer)
    return {"message": "Item added", "item": customer}

