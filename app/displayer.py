from abc import ABC, abstractmethod

from app.book import Book


class BookDisplayer(ABC):
    @staticmethod
    @abstractmethod
    def display(book: Book) -> None:
        pass


class BookConsoleDisplayer(BookDisplayer):
    @staticmethod
    def display(book: Book) -> str:
        print(book.content)


class BookReverseDisplayer(BookDisplayer):
    @staticmethod
    def display(book: Book) -> str:
        print(book.content[::-1])
