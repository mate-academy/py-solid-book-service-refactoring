from abc import ABC

from app.book import Book


class Printer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    def print(self: Book) -> None:
        pass


class ConsolePrinter(Printer):
    def print(self: Book) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)


class ReversePrinter(Printer):
    def print(self: Book) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])
