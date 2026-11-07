from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)

    name = Column(
        String,
        nullable=False
    )

    brand = Column(String)

    size = Column(String)

    category = Column(String)

    # Product
    receipt_items = relationship(
        "ReceiptItem",
        back_populates="product"
    )