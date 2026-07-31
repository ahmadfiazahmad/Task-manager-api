# 🚀 Task Manager REST API

A simple RESTful Task Manager API built with **Python** and **FastAPI** as part of the **FlyRank AI Backend Engineering Internship – Assignment 1**.

The API allows users to perform basic CRUD (Create, Read, Update, Delete) operations on tasks. Task data is stored in memory using a Python list, so all data is lost when the server stops.

---

# 📌 Features

- Create a new task
- Get all tasks
- Get a task by ID
- Update an existing task
- Delete a task
- Health check endpoint
- Automatic Swagger API documentation
- Input validation
- Proper HTTP status codes

---

# 🛠️ Technologies Used

- Python 3
- FastAPI
- Uvicorn
- Pydantic
- Git

---

# 📁 Project Structure

```
Assignment_no_1/
│
├── app/
│   └── main.py
│
├── requirements.txt
├── README.md
├── .gitignore
└── .venv/
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone <repository-url>
cd Assignment_no_1
```

---

## 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

---

## 3. Activate the Virtual Environment

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Run the Server

```bash
uvicorn app.main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

# 📖 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API information |
| GET | `/health` | Health check |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{task_id}` | Get a task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

---

# 📥 Example Request

### Create Task

**POST** `/tasks`

Request Body

```json
{
    "title": "Complete FlyRank Assignment"
}
```

Response

```json
{
    "id": 1,
    "title": "Complete FlyRank Assignment",
    "done": false
}
```

---

# ✅ HTTP Status Codes

| Status Code | Description |
|--------------|-------------|
| 200 OK | Successful request |
| 201 Created | Task created successfully |
| 204 No Content | Task deleted successfully |
| 400 Bad Request | Invalid input |
| 404 Not Found | Task not found |

---

# 📌 Notes

- Tasks are stored in memory using a Python list.
- No database is used.
- Restarting the server clears all tasks.
- This project is intended for learning FastAPI fundamentals and REST API development.

---

# 👨‍💻 Author

**Ahmad**

