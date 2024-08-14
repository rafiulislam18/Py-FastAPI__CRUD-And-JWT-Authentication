from fastapi import FastAPI, Path

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
def get_student(student_id: int = Path(..., description="The ID of the student you want to view", gt=0, lt=3)):
    return students[student_id]
