from pydantic import BaseModel

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