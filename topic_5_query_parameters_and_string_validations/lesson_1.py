from fastapi import FastAPI

app = FastAPI()

# Lesson: Query Parameters and String Validations
# Explanation: This lesson demonstrates how to use query parameters in FastAPI. It shows a basic example where the query parameter 'q' is optional.

@app.get("/items/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
