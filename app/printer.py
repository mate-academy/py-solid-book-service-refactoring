from abc import ABC, abstractmethod

from app.book import Book


class Printer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def printer(self: Book) -> None:
        pass


class ConsolePrinter(Printer):
    def printer(self: Book) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)


class ReversePrinter(Printer):
    def printer(self: Book) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])
