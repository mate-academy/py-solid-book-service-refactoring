from abc import ABC, abstractmethod

from app.books import Book


class DisplayService(ABC):

    @staticmethod
    @abstractmethod
    def display(book: Book) -> None:
        pass


class ConsoleDisplayService(DisplayService):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content)


class ReverseDisplayService(DisplayService):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content[::-1])
