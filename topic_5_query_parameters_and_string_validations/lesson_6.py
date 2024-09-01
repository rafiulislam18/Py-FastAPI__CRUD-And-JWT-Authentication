# Lesson Name : Pydantic v1 regex instead of pattern
# Note : Before Pydantic version 2 and before FastAPI 0.100.0, the parameter was called regex instead of pattern, but it's now deprecated.

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None, Query(min_length=3, max_length=50, regex="^fixedquery$")
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# But know that this is deprecated and it should be updated to use the new parameter pattern.