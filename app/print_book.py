from abc import ABC, abstractmethod

from app.book import Book
from app.display_book import Displayer


class Printer(ABC):
    @abstractmethod
    def print(self) -> None:
        pass


class BookConsolePrinter(Printer):
    def __init__(self, book: Book, displayer: Displayer) -> None:
        self.book = book
        self.displayer = displayer

    def print(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        self.displayer.display()


class BookReversePrinter(BookConsolePrinter):
    def print(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        self.displayer.display()
