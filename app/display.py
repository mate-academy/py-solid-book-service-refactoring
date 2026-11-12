from app.models import Book
from abc import ABC, abstractmethod


class BookDisplay(ABC):
    @abstractmethod
    def display(self, book: "Book") -> None:
        pass


class BookConsoleDisplay(BookDisplay):
    def display(self, book: "Book") -> None:
        print(book.content)


class BookReverseDisplay(BookDisplay):
    def display(self, book: "Book") -> None:
        print(book.content[::-1])
