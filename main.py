#uvicorn main:app --reload --host 0.0.0.0 --port 8000
#gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/greet/{name}") #path parameter
async def greet(name: str, age: int, gender: Optional[str] = "male") -> dict: #query parameter and default parameter
    #/greet/abcd?age=18&gender=female
    return {"message" : f"Hello {name}", "age" : age, "gender" : gender}

class BookCreateModel(BaseModel):
    title: str
    author: str

@app.post("/create_user")
async def create_user(book_data: BookCreateModel):
    #requests.post(url, json=payload)
    return {
        "title" : book_data.title,
        "author" : book_data.author
    }

@app.get("/get_header", status_code = 200)
async def get_header(accept: str = Header(None),
                     content_type: str = Header(None),
                     user_agent: str = Header(None),
                     host: str = Header(None)):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type 
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host
    return request_headers