from abc import ABC
from app.book import Book


class PrintBook(ABC):
    pass


class PrintBookInConsole(PrintBook):
    def __init__(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintBookInReverse(PrintBook):
    def __init__(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
