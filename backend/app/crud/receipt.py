from sqlalchemy.orm import Session
from app.models.receipt import Receipt
from app.models.store import Store
from app.schemas.receipt import ReceiptCreate

def create_receipt(
        db:Session,
        receipt:ReceiptCreate
):
    db_receipt = Receipt(
        store = (
            db.query(Store)
            .filter(Store.id == receipt.store_id)
            .first()
        )
    )