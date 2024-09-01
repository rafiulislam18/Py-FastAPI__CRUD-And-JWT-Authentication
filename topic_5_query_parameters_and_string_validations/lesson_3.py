# Lesson Name : Add Query to Annotated in the q parameter
# Note : Now that we have this Annotated where we can put more information (in this case someadditional validation), add Query inside of Annotated, and set the parameter max_length to 50.

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Notice that the default value is still None, so the parameter is still optional.