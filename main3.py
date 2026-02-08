from fastapi import FastAPI

from src1.routers import book_router

version = "v1"

app = FastAPI(
    title = "Books",
    description = "API for books management system",
    version = version
)

app.include_router(book_router, prefix=f"/api/{version}", tags=["books"]) #add /api/{version}/books to access the book methods


