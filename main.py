from fastapi import FastAPI,HTTPException
from typing import List
from models import Product, ProductUpdateRequest

app=FastAPI()

db: List[Product]=[
    Product(
        id=1,
        name="Laptop",
        quantity=100,
        price=150000        
    ),
    Product(
        id=2,
        name="Mobile",
        quantity=20,
        price=15000        
    )
]

@app.get("/")
def root():
    return{"Hello":"World"}

@app.get("/products")
async def fetch_products():
    return db

@app.post("/products")
async def new_product(product:Product):
    db.append(product)
    return {"id":product.id}


@app.delete("/products/{product_id}")
async def delete_product(product_id:int):
    for product in db:
        if product.id==product_id:
            db.remove(product)
            return{"message":"Deleted Successfully"}
    raise HTTPException(
        status_code=404,
        detail=f"Product with id:{product_id} does not exists"
    )   
    
@app.put("/products/{product_id}")
async def update_product(product_id:int,product_update: ProductUpdateRequest):
        for i,product in enumerate(db):
            if product.id==product_id:
                updated_product=Product(
                    id=product.id,
                    name=product_update.name if product_update.name is not None else product.name,
                    quantity=product_update.quantity if product_update.quantity is not None else product.quantity,
                    price=product_update.price if product_update.price is not None else product.price
                    
                )
                db[i]=updated_product
                return updated_product
        raise HTTPException(
        status_code=404,
        detail=f"Product with id:{product_id} does not exists"
    )   
                  
                 