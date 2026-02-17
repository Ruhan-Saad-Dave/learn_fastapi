from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List

from src2.books.services import BooksService
from src2.books.schemas import Books, UpdateBooks
from src2.db.main import get_session 

book_router = APIRouter(
    prefix="/books"
)
book_service = BooksService()

@book_router.get('/', response_model=List[Books])
async def get_all_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books 

@book_router.get('/{book_uid}')
async def get_a_book(book_uid: str, session: AsyncSession=Depends(get_session)) -> dict:
    book = await book_service.get_book(book_uid, session)
    if book is not None:
        return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail = "Book not found") #when the data isn't available

@book_router.post('/', status_code=status.HTTP_201_CREATED, response_model=Books)
async def create_a_book(book_data: Books, session: AsyncSession=Depends(get_session))->dict:
    new_book = book_service.create_book(book_data, session)
    return new_book

@book_router.put('/{book_uid}') #full replacement
async def update_entire_book(book_uid: str) -> dict:
    pass 

@book_router.patch('/{book_uid}') #partial replacement
async def update_partial_book(book_uid: str, book_update: UpdateBooks, session: AsyncSession=Depends(get_session)) -> dict:
    updated_book = await book_service.update_book(book_uid, book_update, session)
    if updated_book is not None:
        return updated_book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail = "Book not found")

@book_router.delete('/{book_uid}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_uid: str, session: AsyncSession=Depends(get_session)):
    status = await book_service.delete_book(book_uid, session)
    if status:
        return None
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail = "Book not found")