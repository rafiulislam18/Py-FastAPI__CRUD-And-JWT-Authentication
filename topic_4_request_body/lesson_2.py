# Lesson Name : Request body + path parameters
# Note : You can declare path parameters and request body at the same time.

"""
FastAPI will recognize that the function parameters that match path parameters should be taken from the path,
and that function parameters that are declared to be Pydantic models should be taken from the request body.
"""

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}
