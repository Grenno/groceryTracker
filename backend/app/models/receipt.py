from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Numeric,
    DateTime
)

from sqlalchemy.orm import relationship

from app.database import Base


class Receipt(Base):
    __tablename__ = "receipts"

    id = Column(Integer, primary_key=True)

    store_id = Column(
        Integer,
        ForeignKey("stores.id")
    )

    store = relationship(
        "Store",
        back_populates="receipts"
    )

    items = relationship(
        "ReceiptItem",
        back_populates="receipt"
    )

    payment_type = Column(String, nullable=False)

    purchase_date = Column(
        DateTime,
        nullable=False
    )

    discount_amount = Column(
        Numeric(10, 2),
        nullable=True
    )

    subtotal = Column(
        Numeric(10, 2),
        nullable=False
    )

    tax_amount = Column(
        Numeric(10, 2),
        nullable=False
    )

    total_amount = Column(
        Numeric(10, 2),
        nullable=False
    )