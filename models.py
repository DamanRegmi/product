from pydantic import BaseModel
from typing import Optional
class Product(BaseModel):
    id: int
    name:str
    #description:str
    quantity:int
    price:int
    
class ProductUpdateRequest(BaseModel):
    name:   Optional[str]=None
    quantity:   Optional[int]=None
    price:   Optional[int]=None