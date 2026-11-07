from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

# store table 
class Store(Base):
   __tablename__ = "stores"

   id = Column(Integer, primary_key=True)
   name = Column(String, nullable=False)
   # address can be null if location not provided sufficiently
   address = Column(String)

   receipts = relationship(
      "Receipt",
      back_populates="store"
   )


# receipt table
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

   items =relationship(
      "ReceiptItem",
      back_populates="receipt"
   )

   payment_type = Column(String, nullable=False)

   purchase_date = Column(DateTime, nullable=False)

   # (10,2) signals numeric place i.e. 1111111111.00
   discount_amount = Column(Numeric(10,2), nullable=True)

   subtotal = Column(Numeric(10,2), nullable=False)

   tax_amount = Column(Numeric(10,2), nullable=False)

   total_amount = Column(Numeric(10,2), nullable=False)


# receipt items table
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



   quantity = Column(Numeric(10, 3), nullable=False)

   unit_price = Column(Numeric(10, 2), nullable=False)

   unit_of_measure = Column(String)

   line_total = Column(Numeric(10, 2), nullable=False)

    # deposit and recycle fee on some recyclable products
   deposit = Column(Numeric(10, 2), nullable=True)

   recycle_fee = Column(Numeric(10,2), nullable=True)

# product table
class Product(Base):
   __tablename__ = "products"

   id = Column(Integer, primary_key=True)

   name = Column(String, nullable=False)

   brand = Column(String, nullable=True)

   size = Column(String)

   category = Column(String)

   