from fastapi import APIRouter, HTTPException
from .schemas.product import Product

prod_router = APIRouter(
    prefix="/products",
    tags=["product"]
    )

products = []

@prod_router.get("/")
async def get_products():
    return products

@prod_router.get("/{id}")
async def get_product(product_id: int):
    for prd in products:
        if prd.id == product_id:
            return prd
    
    raise HTTPException(status_code=404, detail="Item not found")


@prod_router.post("/")
async def create_item(prd: Product):
    products.append(prd)
    return {"message": "Item added", "item": prd}

