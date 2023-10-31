from abc import ABC, abstractmethod

from app.book import Book


class DisplayProcessor(ABC):
    @staticmethod
    @abstractmethod
    def display(book: Book) -> None:
        pass


class DisplayConsoleProcessor(DisplayProcessor):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content)


class DisplayReverseProcessor(DisplayProcessor):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content[::-1])
