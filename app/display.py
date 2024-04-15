from abc import ABC, abstractmethod

from app.book import Book


class PrintBook(ABC):

    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def display(self: Book) -> str:
        pass


class ConsoleDisplay:

    def display(self: Book) -> None:
        print(self.content)


class ReverseDisplay:

    @staticmethod
    def display(self: Book) -> None:
        print(self.content[::-1])
