from abc import ABC, abstractmethod

from app.models import Book


class BookDisplay(ABC):
    @staticmethod
    @abstractmethod
    def display(book: Book) -> None:
        pass


class ConsoleBookDisplay(BookDisplay):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content)


class ReverseBookDisplay(BookDisplay):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content[::-1])
