# Lesson Name : Request Body
# Note : When you need to send data from a client (let's say, a browser) to your API, you send it as a request body.

"""
Import Pydantic's BaseModel

Create your data model

Declare it as a parameter

Use the model
"""

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# Inside of the function, you can access all the attributes of the model object directly.