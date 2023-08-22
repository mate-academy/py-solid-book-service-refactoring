from abc import ABC, abstractmethod

from app.book import Book


class BookDisplay(ABC):
    @staticmethod
    @abstractmethod
    def display(book: Book):
        pass


class BookDisplayConsole(BookDisplay):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content)


class BookDisplayReverse(BookDisplay):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content[::-1])
