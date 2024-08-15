from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

students = {
    1: {
        "name": "Rafi",
        "age": 21,
        "class": "B.Sc in CSE"
    }
}

# Basic API
@app.get("/")
def index():
    return {"name": "First Data"}

# Path Parameter
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student you want to view", gt=0, lt=3)):
    return students[student_id]

# Query Parameter (+ Path Parameter)
@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, text : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

