# Lesson Name : Using just list
# Note : You can also use list directly instead of List[str] (or list[str] in Python 3.9+).

from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[list, Query()] = []):
    query_items = {"q": q}
    return query_items

"""
Keep in mind that in this case, FastAPI won't check the contents of the list.
For example, List[int] would check (and document) that the contents of the list are integers. But list alone wouldn't.
"""