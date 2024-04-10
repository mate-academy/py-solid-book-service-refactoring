from app.main import Book


class Base:
    def __init__(self, book: Book) -> None:
        self.book = book
