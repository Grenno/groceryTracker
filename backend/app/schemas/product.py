# app/schemas/product.py

from pydantic import BaseModel



class ProductBase(BaseModel):
    name: str
    brand: str | None = None
    size: str | None = None
    category: str | None = None


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True
