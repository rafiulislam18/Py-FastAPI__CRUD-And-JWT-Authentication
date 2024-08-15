from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "Rafi",
        "age": 21,
        "year": "B.Sc in CSE"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

# FastAPI - Basic API
@app.get("/")
def index():
    return {"name": "First Data"}

# FastAPI - Path Parameter
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student you want to view", gt=0, lt=3)):
    return students[student_id]

# FastAPI - Query Parameter (+ Path Parameter)
@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, text : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

# FastAPI - Request Body
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    students[student_id] = student
    return students[student_id]