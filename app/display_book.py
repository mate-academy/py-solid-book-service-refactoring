from abc import ABC
from app.book import Book


class DisplayBook(ABC):
    pass


class DisplayBookInConsole(DisplayBook):
    def __init__(self, book: Book) -> None:
        print(book.content)


class DisplayBookInReverse(DisplayBook):
    def __init__(self, book: Book) -> None:
        print(book.content[::-1])
