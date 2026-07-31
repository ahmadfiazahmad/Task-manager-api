from fastapi import FastAPI

app = FastAPI()

# In-memory storage for tasks.
tasks = []


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