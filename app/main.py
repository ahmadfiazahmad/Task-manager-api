from fastapi import FastAPI

# Create the FastAPI application.
app = FastAPI()


# Root endpoint.
@app.get("/")
def root():
    return {
        "message": "Hello, FlyRank Backend Internship!"
    }