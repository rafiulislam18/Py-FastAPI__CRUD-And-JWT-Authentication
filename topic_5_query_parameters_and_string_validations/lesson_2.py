# Lesson Name : Additional validation
# Note : We are going to enforce that even though q is optional, whenever it is provided, its length doesn't exceed 50 characters.

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results



# We had this type annotation:
# q: str | None = None

# What we will do is wrap that with Annotated, so it becomes:
# q: Annotated[str | None] = None

# Both of those versions mean the same thing, q is a parameter that can be a str or None, and by default, it is None.