# Lesson Name : Query parameter list / multiple values with defaults
# Note : And you can also define a default list of values if none are provided.

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items

"""
If you go to:
http://localhost:8000/items/

the default of q will be: ["foo", "bar"] and your response will be:
{
  "q": [
    "foo",
    "bar"
  ]
}
"""
