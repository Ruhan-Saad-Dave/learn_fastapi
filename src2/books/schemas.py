from pydantic import BaseModel
from datetime import datetime
import uuid

class Books(BaseModel):
    uid : uuid.UUID
    title : str 
    publisher : str 
    published_date : str 
    page_count : int
    author : str 
    language : str
    created_at: datetime
    updated_at: datetime

class CreateBooks(BaseModel):
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