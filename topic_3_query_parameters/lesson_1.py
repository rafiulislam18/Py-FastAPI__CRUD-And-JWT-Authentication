# Lesson Name : Query Parameters
# Note : When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

"""
The query is the set of key-value pairs that go after the ? in a URL, separated by & characters.

For example, in the URL:
http://127.0.0.1:8000/items/?skip=0&limit=10

...the query parameters are:
skip: with a value of 0
limit: with a value of 10
"""