# Lesson Name : Path parameters with types
# Note : You can declare the type of a path parameter in the function, using standard Python type annotations.

from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

"""
In this case, item_id is declared to be an int.

Notice that the value your function received (and returned) is 3, as a Python int, not a string "3".
So, with that type declaration, FastAPI gives you automatic request "parsing".
"""
