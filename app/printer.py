from abc import ABC, abstractmethod

from app.book import Book
from app.formatter import Formatter


class Printer(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass

    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsolePrinter(Printer):
    def __init__(self, formatter_class: Formatter) -> None:
        self.formatter = formatter_class()

    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        self.display(book)

    def display(self, book: Book) -> None:
        content = self.formatter.format(book.content)
        print(content)
