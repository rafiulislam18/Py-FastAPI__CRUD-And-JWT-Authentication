# Lesson Name : First Steps
# Note : The simplest FastAPI file could look like this.

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

"""
Run in development mode, command :
fastapi dev main.py

Run in production mode, command :
fastapi run main.py

You will see the JSON response as :
{"message": "Hello World"}

Interactive API docs :
http://127.0.0.1:8000/docs

Alternative API docs :
http://127.0.0.1:8000/redoc
"""
