# Lesson Name : Exclude parameters from OpenAPI
# Note : To exclude a query parameter from the generated OpenAPI schema (and thus, from the automatic documentation systems), set the parameter include_in_schema of Query to False.

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    hidden_query: Annotated[str | None, Query(include_in_schema=False)] = None,
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}

"""
In this example, the hidden_query parameter will not appear in the API documentation (OpenAPI schema),
but it can still be used when making requests to the /items/ endpoint.
This is particularly useful for internal parameters or those you want to phase out without publicly documenting them.
"""
