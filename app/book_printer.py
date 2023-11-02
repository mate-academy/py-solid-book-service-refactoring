from abc import ABC, abstractmethod

from app.book import Book


class Printer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def print(self) -> None:
        pass


class ConsolePrint(Printer):
    def print(self) -> None:
        print(f"Printing the book: {self.book.get_title()}...")
        print(self.book.get_content())


class ReversePrint(Printer):
    def print(self) -> None:
        print(f"Printing the book in reverse: {self.book.get_title()}...")
        print(self.book.get_content()[::-1])
