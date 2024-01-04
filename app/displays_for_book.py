from abc import ABC, abstractmethod

from app.book_class import Book


class DisplayStrategy(ABC):
    @staticmethod
    @abstractmethod
    def display(book: Book) -> None:
        pass


class ConsoleDisplay(DisplayStrategy):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content[::-1])
