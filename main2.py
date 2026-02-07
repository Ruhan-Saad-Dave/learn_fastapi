from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List

books = [
    {
      "id": 1,
      "title": "The Echoes of Silence",
      "publisher": "Blue Horizon Press",
      "published_date": "2023-05-12",
      "page_count": 320,
      "author": "Elena Vance",
      "language": "English"
    },
    {
      "id": 2,
      "title": "Quantum Mechanics for Poets",
      "publisher": "Academic Spark",
      "published_date": "2021-11-30",
      "page_count": 215,
      "author": "Dr. Aris Thorne",
      "language": "English"
    },
    {
      "id": 3,
      "title": "Le Mystère de l'Ombre",
      "publisher": "Éditions du Ciel",
      "published_date": "2022-08-15",
      "page_count": 412,
      "author": "Julien Beaumont",
      "language": "French"
    },
    {
      "id": 4,
      "title": "The Digital Renaissance",
      "publisher": "TechNode Media",
      "published_date": "2024-01-10",
      "page_count": 288,
      "author": "Sarah Jenkins",
      "language": "English"
    },
    {
      "id": 5,
      "title": "Crónicas de un Viajero",
      "publisher": "Sol de España",
      "published_date": "2020-03-22",
      "page_count": 550,
      "author": "Mateo Rivera",
      "language": "Spanish"
    }
]


app = FastAPI()

class Books(BaseModel):
    id : int
    title : str 
    publisher : str 
    published_date : str 
    page_count : int
    author : str 
    language : str

class UpdateBooks(BaseModel):
    title : str 
    publisher : str 
    page_count : int
    author : str 
    language : str

@app.get('/books', response_model=List[Books])
async def get_all_books():
    return books 

@app.get('/books/{book_id}')
async def get_a_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail = "Book not found") #when the data isn't available

@app.post('/books', status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Books)->dict:
    new_book = book_data.model_dump() #converts it into dictionary
    books.append(new_book)
    return new_book

@app.put('/books/{book_id}') #full replacement
async def update_entire_book(book_id: int) -> dict:
    pass 

@app.patch('/books/{book_id}') #partial replacement
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

@app.delete('/books/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail = "Book not found")