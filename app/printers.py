from abc import ABC, abstractmethod

from app.displays import BookDisplayConsole, BookDisplayReverse
from app.models import Book


class Printer(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class BookPrintConsole(Printer):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        BookDisplayConsole().display(book)


class BookPrintReverse(Printer):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        BookDisplayReverse().display(book)
