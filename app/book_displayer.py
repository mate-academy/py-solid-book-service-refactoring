from abc import ABC, abstractmethod

from .book import Book


class Displayer(ABC):
    @staticmethod
    @abstractmethod
    def display(book: Book) -> None:
        pass


class BookDisplayerConsole(Displayer):
    @staticmethod
    def display_content(book: Book) -> None:
        print(book.content)


class BookDisplayerReverse(Displayer):
    @staticmethod
    def display_content(book: Book) -> None:
        print(book.content[::-1])
