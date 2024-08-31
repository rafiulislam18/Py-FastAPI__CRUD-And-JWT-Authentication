from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

# Lesson: Add Query to Annotated in the `q` Parameter
# Explanation: Combines `Annotated` with `Query` to specify validation rules directly in the function signature.

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
