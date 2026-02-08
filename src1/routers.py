from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from typing import List

from src1.book_data import books
from src1.schemas import Books, UpdateBooks

book_router = APIRouter(
    prefix="/books"
)

@book_router.get('/', response_model=List[Books])
async def get_all_books():
    return books 

@book_router.get('/{book_id}')
async def get_a_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail = "Book not found") #when the data isn't available

@book_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Books)->dict:
    new_book = book_data.model_dump() #converts it into dictionary
    books.append(new_book)
    return new_book

@book_router.put('/{book_id}') #full replacement
async def update_entire_book(book_id: int) -> dict:
    pass 

@book_router.patch('/{book_id}') #partial replacement
async def update_partial_book(book_id: int, book_update: UpdateBooks) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update.title
            book["publisher"] = book_update.title 
            book["page_count"] = book_update.page_count 
            book["language"] = book_update.language 
            return book 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail = "Book not found")

@book_router.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail = "Book not found")