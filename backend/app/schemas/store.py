from pydantic import BaseModel
from app.schemas.receipt import ReceiptResponse



class StoreBase(BaseModel):

    name: str
    address: str | None = None


class StoreCreate(StoreBase):
    pass

class StoreResponse(StoreBase):
    id: int
    # retrieves a list of reciepts tied to the store
    receipts: list[ReceiptResponse] = []

    class Config:
        from_attribute = True