# Lesson Name : Optional parameters
# Note : The same way, you can declare optional query parameters, by setting their default to None.

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}

# In this case, the function parameter q will be optional, and will be None by default.
