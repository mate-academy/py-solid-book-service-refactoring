from abc import ABC, abstractmethod
from app.book_implementation import Book


class DisplayContent(ABC):
    @staticmethod
    @abstractmethod
    def display(book: Book) -> None:
        pass


class ConsoleDisplay(DisplayContent):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayContent):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content[::-1])
