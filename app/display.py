from abc import ABC, abstractmethod

from app.book import Book


class Display(ABC):
    @staticmethod
    @abstractmethod
    def display(book: Book) -> None:
        pass


class DisplayConsole(Display):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content)


class DisplayReverse(Display):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content[::-1])
