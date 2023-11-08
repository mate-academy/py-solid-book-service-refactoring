from abc import ABC, abstractmethod

from app.books import Book


class Printer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def print_book(self: Book) -> None:
        pass


class ConsolePrinter(Printer):
    def print_book(self: Book) -> None:
        print(self.title)
        print(self.content)


class ReversePrinter(Printer):
    def print_book(self: Book) -> None:
        print(self.title)
        print(self.content[::-1])
