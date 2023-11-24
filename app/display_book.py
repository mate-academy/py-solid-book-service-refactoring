from abc import ABC, abstractmethod
from app.book import Book


class DisplayBook(ABC):
    @staticmethod
    @abstractmethod
    def display(book: Book) -> None:
        pass


class DisplayBookInConsole(DisplayBook):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content)


class DisplayBookInReverse(DisplayBook):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content[::-1])
