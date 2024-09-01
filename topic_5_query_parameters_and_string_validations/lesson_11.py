# Lesson Name : Query parameter list / multiple values
# Note : When you define a query parameter explicitly with Query you can also declare it to receive a list of values, or said in another way, to receive multiple values. For example, to declare a query parameter q that can appear multiple times in the URL.

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items

"""
Then, with a URL like:
http://localhost:8000/items/?q=foo&q=bar

you would receive the multiple q query parameters' values (foo and bar) in a Python list inside your path operation function, in the function parameter q

So, the response to that URL would be:
{
  "q": [
    "foo",
    "bar"
  ]
}
"""
