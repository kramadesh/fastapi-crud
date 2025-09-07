from fastapi import FastAPI

from . import database, models
from .routers import books

# Create tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Books CRUD API")

# Register routers
app.include_router(books.router)
