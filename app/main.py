from fastapi import FastAPI, HTTPException,status
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
@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: Task):
    print(">>> create_task() was called")

    if not task.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task title cannot be empty."
        )

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

# Defines the structure of data required to update a task.
class TaskUpdate(BaseModel):
    title: str

# Updates the title of an existing task.
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskUpdate):

    # Prevent empty or whitespace-only task titles.
    if not updated_task.title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task title cannot be empty."
        )

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found"
    )    

# Deletes a task based on its ID.
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return 
                
            

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )