# Lesson Name : Deprecating parameters
# Note : Now let's say you don't like a parameter anymore.

"""
You have to leave it there a while because there are clients using it, but you want the docs to clearly show it as deprecated.

Then pass the parameter deprecated=True to Query
"""

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

"""
Deprecating parameters in FastAPI means marking a query parameter as outdated or no longer recommended for use,
typically signaling that it will be removed in future versions.
This is done using the deprecated=True option in the Query function.
When a parameter is deprecated, it still works, but its usage is discouraged,
and it will be flagged as deprecated in the API documentation.

In this example, the q parameter is marked as deprecated, which will be reflected in the OpenAPI documentation, alerting users to avoid using it in future API calls.
"""
