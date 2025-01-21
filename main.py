import uvicorn
from fastapi import FastAPI, HTTPException

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

@app.get("/")
def home():
    return ("Hello world!!!!")

# получить все книги
@app.get("/books")
def read_books():
    return books

# получить книгу по id
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

