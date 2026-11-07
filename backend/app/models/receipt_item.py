from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Numeric
)

from sqlalchemy.orm import relationship

from app.database import Base


class ReceiptItem(Base):
    __tablename__ = "receipt_items"

    id = Column(Integer, primary_key=True)

    receipt_id = Column(
        Integer,
        ForeignKey("receipts.id")
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id")
    )

    receipt = relationship(
        "Receipt",
        back_populates="items"
    )

    quantity = Column(
        Numeric(10, 3),
        nullable=False
    )

    unit_price = Column(
        Numeric(10, 2),
        nullable=False
    )

    unit_of_measure = Column(String)

    line_total = Column(
        Numeric(10, 2),
        nullable=False
    )

    deposit = Column(
        Numeric(10, 2),
        nullable=True
    )

    recycle_fee = Column(
        Numeric(10, 2),
        nullable=True
    )

    # ReceiptItem
    product = relationship(
        "Product",
        back_populates="receipt_items"
    )