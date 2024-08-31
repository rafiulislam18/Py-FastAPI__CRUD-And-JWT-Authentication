# Lesson Name : Query Parameters and String Validations
# Note : FastAPI allows you to declare additional information and validation for your parameters.

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results