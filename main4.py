from fastapi import FastAPI
from contextlib import asynccontextmanager 

from src2.books.routers import book_router
from src2.db import init_db

@asynccontextmanager
async def life_span():
    print(f"The server is starting ...")
    await init_db
    yield 
    print(f"The server has stopped.")

version = "v1"

app = FastAPI(
    title = "Books",
    description = "API for books management system",
    version = version,
    lifespan = life_span
)

app.include_router(book_router, prefix=f"/api/{version}", tags=["books"]) #add /api/{version}/books to access the book methods


