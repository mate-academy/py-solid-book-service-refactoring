from abc import ABC, abstractmethod

from app.model import Book


class Printer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def printer(self) -> None:
        ...


class ConsolePrinter(Printer):
    def printer(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class ReversePrinter(Printer):
    def printer(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])
