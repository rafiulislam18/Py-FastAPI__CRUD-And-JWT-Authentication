from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

# Lesson: Use Annotated in the Type for the `q` Parameter
# Explanation: Demonstrates using `Annotated` to combine type hints with query validation. This example ensures 'q' is a string with a max length constraint.

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
