from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel

class ReceiptBase(BaseModel):

    store_id: int
    payment_type: str
    purchase_date: datetime
    discount_amount: Decimal | None = None
    subtotal: Decimal
    tax_amount: Decimal
    total_amount: Decimal

class ReceiptCreate(ReceiptBase):
    pass

class ReceiptResponse(ReceiptBase):
    id: int
    store_id: int

    class Config:
        from_attributes = True