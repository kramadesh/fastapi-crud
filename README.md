
# 📚 FastAPI Books CRUD API

A simple and well-structured **FastAPI** application that provides **CRUD operations** for managing books, using:

- **FastAPI** for API development
- **SQLAlchemy** ORM with SQLite
- **Pydantic** for schema validation
- **Pytest** for testing

---

## 📂 Project Structure

app/

│── main.py # FastAPI entry point

│── database.py # DB connection and session

│── models.py # SQLAlchemy models

│── schemas.py # Pydantic schemas

│── crud.py # CRUD operations

│── routers/

│ └── books.py # Books API routes

tests/

│── test_books.py # Pytest unit tests

pyproject.toml # Dependencies


---

## ⚙️ Installation

### 1️⃣ Clone the repository
bash
git clone https://github.com/kramadesh/fastapi-crud.git
cd fastapi-crud

## ⚙️ Running the App

python run.py

API will be available at:

Swagger Docs 👉 http://127.0.0.1:8000/docs


uv init crud_project
uv venv
.venv\Scripts\activate
cd crud_project
#copy pyproject.toml
uv sync --active

python run.py
