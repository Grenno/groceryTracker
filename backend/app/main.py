from fastapi import FastAPI
from app.database import engine, Base
from app.models import Store

app = FastAPI()

# creates tables in database specific to this db connection
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Grocery Tracker API"}