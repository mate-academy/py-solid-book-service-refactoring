from abc import ABC

from app.book import Book


class Display(ABC):
    @staticmethod
    def display(book: Book) -> None:
        pass


class ConsoleDisplay(Display):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content)


class ReverseDisplay(Display):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content[::-1])
