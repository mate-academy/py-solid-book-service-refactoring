from abc import ABC, abstractmethod

from app.display import DisplayContent
from app.models import Book


class PrintBook(ABC):
    def __init__(self, method: DisplayContent) -> None:
        self.method = method

    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class ConsolePrintBook(PrintBook):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        self.method.display(book)


class ReversePrintBook(PrintBook):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        self.method.display(book)
