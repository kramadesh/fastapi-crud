
# 📚 FastAPI Books CRUD API

A simple and well-structured **FastAPI** application that provides **CRUD operations** for managing books, using:

- **FastAPI** for API development
- **SQLAlchemy** ORM with SQLite
- **Pydantic** for schema validation
- **Pytest** for testing

---

## 📂 Project Structure

app/ <br>
│── main.py # FastAPI entry point <br>
│── database.py # DB connection and session <br>
│── models.py # SQLAlchemy models <br>
│── schemas.py # Pydantic schemas <br>
│── crud.py # CRUD operations <br>
│── routers/ <br>
│ └── books.py # Books API routes <br>
tests/ <br>
│── conftest.py # pytest setup <br>
│── test_books.py # Pytest unit tests <br>
pyproject.toml # Dependencies <br>
pytest.ini #


---

## ⚙️ Installation

### 1️⃣ Clone the repository
bash
git clone https://github.com/kramadesh/fastapi-crud.git <br>
cd fastapi-crud <br>

### 1️2️⃣ Create a virtual environment

python -m venv <br>
source .venv/bin/activate   # On Linux/Mac <br>
.venv\Scripts\activate      # On Windows <br>


### 3️⃣ Install dependencies

uv sync --active <br>

## ⚙️ Running the App

python run.py

API will be available at:

Swagger Docs 👉 http://127.0.0.1:8000/docs




