from abc import ABC, abstractmethod

from app.book import Book


class Display(ABC):
    @staticmethod
    @abstractmethod
    def display_content(book: Book) -> None:
        pass


class ConsoleDisplay(Display):
    @staticmethod
    def display_content(book: Book) -> None:
        print(book.content)


class ReverseDisplay(Display):
    @staticmethod
    def display_content(book: Book) -> None:
        print(book.content[::-1])
