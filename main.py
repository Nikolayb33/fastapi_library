import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


books = [
    {
        "id": 1,
        "title": "Labirint",
        "autor": "Lukyanenko",
    },
    {
        "id": 2,
        "title": "Sbornik",
        "autor": "Turgenev",
    }
]

@app.get("/books",
         tags=["books"],
         summary="get all books")
def read_books():
    return books


@app.get("/books/{book_id}",
         tags=["books"],
         summary= "get book from id")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="book not found")


class NewBook(BaseModel):
    title: str
    author: str

@app.post("/books",
          tags= ["books"])
def create_book(new_book: NewBook):
    books.append({
        "id": len(books) + 1,
        "title": new_book.title,
        "author": new_book.author,
    })
    return {"success": True, "message": "book add"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

