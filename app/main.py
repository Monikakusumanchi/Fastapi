from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()

item_master = {1 :'This is Paris',
                2 :'This is France',
                3 :'This is Aus',
                4 :'This is Indoneshia',
                5 :'this is London'}

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items")
async def items():

    return {"items": item_master}

@app.get("/items/{item_id}")
async def get_item(item_id: int,  short: bool): 
    if short == True  : 
        return {"item": item_master[item_id]}
    else:
        return {"item": "This is a long description"}

@app.post("/items")
async def create_item(item: Item):
    return item

  



