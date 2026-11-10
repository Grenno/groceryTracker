from pydantic import BaseModel
from decimal import Decimal



class ReceiptItemBase(BaseModel):

    receipt_id : int
    product_id : int
    quantity : Decimal
    unit_price : Decimal
    unit_of_measure : str | None = None
    line_total : Decimal
    deposit : Decimal | None = None
    recycle_fee : Decimal | None = None

class ReceiptItemCreate(ReceiptItemBase):
    pass

class ReceiptItemResponse(ReceiptItemBase):
    id : int

    class Config:
        from_attributes = True
