from fastapi import FastAPI, Query

app = FastAPI()

# Lesson: Alternative (Old): Query as the Default Value
# Explanation: Demonstrates an older method where `Query` is used directly to specify the default value and validation rules.

@app.get("/items/")
async def read_items(q: str | None = Query(None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
