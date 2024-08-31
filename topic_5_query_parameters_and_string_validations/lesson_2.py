from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

# Lesson: Additional Validation
# Explanation: This lesson introduces additional validation by setting a maximum length constraint on the query parameter 'q'.

@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
