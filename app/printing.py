from abc import ABC, abstractmethod

from app.book import Book


class Printer(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def print_book(self) -> None:
        pass


class ConsolePrint(Printer):
    def print_book(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class ReversePrint(Printer):
    def print_book(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])
