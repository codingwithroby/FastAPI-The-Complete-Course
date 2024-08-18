from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author 1", "category": "Science"},
    {"title": "Title Two", "author": "Author 2", "category": "Maths"},
    {"title": "Title 3", "author": "Author 3", "category": "Geography"},
    {"title": "Title 4", "author": "Author 4", "category": "Economics"},
    {"title": "Title 5", "author": "Author 5", "category": "Science"},
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.get("/books/{bookTitle}")
async def read_all_books(bookTitle: str):
    booksInSelectedCategory = []
    for book in BOOKS:
        if book["title"].casefold() == bookTitle.casefold():
            booksInSelectedCategory.append(book)

    if len(booksInSelectedCategory) > 0:
        return booksInSelectedCategory
    else:
        return {f"No book present with this bookTitle: {bookTitle}"}


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book["category"].casefold() == category.casefold():
            books_to_return.append(book)

    if len(books_to_return) > 0:
        return books_to_return
    else:
        return {f"No book present with this book category: {category}"}


@app.get("/books/{bookAuthor}/")
async def read_all_books(bookAuthor: str, category: str):
    booksInSelectedCategory = []
    for book in BOOKS:
        if (
            book["author"].casefold() == bookAuthor.casefold()
            and book["category"].casefold() == category.casefold()
        ):
            booksInSelectedCategory.append(book)

    if len(booksInSelectedCategory) > 0:
        return booksInSelectedCategory
    else:
        return {f"No book present with this bookAuthor: {bookAuthor}"}


@app.get("/books/by_author/{authorName}")
async def get_books_by_author(authorName: str):
    booksByAuthor = []
    for book in BOOKS:
        if book["author"].casefold() == authorName.casefold():
            booksByAuthor.append(book)

    return booksByAuthor


@app.post("/books/createBook")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return BOOKS


@app.put("/books/update_book/{book_title}")
async def update_book(book_title: str, update=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i]["title"].casefold() == book_title.casefold():
            BOOKS[i]["author"] = update["author"]
            BOOKS[i]["category"] = update["category"]

            return BOOKS[i]


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i]["title"].casefold() == book_title.casefold():
            del BOOKS[i]
            break

    return BOOKS
