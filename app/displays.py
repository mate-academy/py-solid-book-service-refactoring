from abc import ABC, abstractmethod
from app.book import Book


class BookDisplay(ABC):
    @staticmethod
    @abstractmethod
    def display(book: Book) -> None:
        ...


class ConsoleDisplay(BookDisplay):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content)


class ReverseDisplay(BookDisplay):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content[::-1])
