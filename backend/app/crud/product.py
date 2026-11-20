from sqlalchemy.orm import Session
from app.models.product import Product
from app.schemas.product import ProductCreate

def create_product(
        db: Session,
        product: ProductCreate
):

    db_product = Product(
        name=product.name,
        brand=product.brand,
        size=product.size,
        category=product.category
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product

def get_product(
        db: Session,
        product_id: int
):
    return db.query(Product).filter(
        Product.id == product_id
    ).first()

def get_products(
    db: Session
):
    return db.query(Product).all()

def delete_product(
    db: Session,
    product_id: int
):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if product:
        db.delete(product)
        db.commit()

    return product