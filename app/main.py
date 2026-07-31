from fastapi import FastAPI

app = FastAPI()


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