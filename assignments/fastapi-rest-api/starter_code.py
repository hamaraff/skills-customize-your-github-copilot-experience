from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    year: int
    description: Optional[str] = None

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None
    description: Optional[str] = None

books = [
    {"id": 1, "title": "The Pragmatic Programmer", "author": "Andrew Hunt", "year": 1999, "description": "A guide to pragmatic software development."},
    {"id": 2, "title": "Clean Code", "author": "Robert C. Martin", "year": 2008, "description": "A handbook of agile software craftsmanship."},
]

@app.get("/books", response_model=List[Book])
def get_books():
    return books

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=Book, status_code=201)
def create_book(book: Book):
    new_id = max([b["id"] for b in books]) + 1 if books else 1
    book_data = book.dict()
    book_record = {"id": new_id, **book_data}
    books.append(book_record)
    return book_record

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: BookUpdate):
    for book in books:
        if book["id"] == book_id:
            update_data = book_update.dict(exclude_unset=True)
            if not update_data:
                raise HTTPException(status_code=400, detail="No update data provided")
            book.update(update_data)
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            books.pop(index)
            return
    raise HTTPException(status_code=404, detail="Book not found")
