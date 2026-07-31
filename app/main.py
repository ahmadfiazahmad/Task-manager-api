from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory storage for tasks.
tasks = []
# Defines the structure of data required to create a new task.
class Task(BaseModel):
    title: str


@app.get("/")
def root():
    return {
        "application": "Task Manager API",
        "version": "1.0.0",
        "status": "Running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "Healthy"
    }

@app.get("/tasks")
def get_tasks():
    return tasks


# Creates a new task and stores it in memory.
@app.post("/tasks")
def create_task(task: Task):

    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "done": False
    }

    tasks.append(new_task)

    return new_task


# Returns a single task based on its ID.
@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
