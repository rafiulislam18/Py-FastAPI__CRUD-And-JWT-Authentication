from fastapi import FastAPI

app = FastAPI()

students = {
    1: {
        "name": "Rafiul Islam",
        "age": 21,
        "class": "B.Sc in CSE"
    }
}

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id]