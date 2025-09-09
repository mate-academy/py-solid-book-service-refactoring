from abc import ABC, abstractmethod
from .models import Book
from .strategies import DisplayStrategy


class Printer(ABC):
    @abstractmethod
    def print(self, book: Book, strategy: DisplayStrategy) -> None:
        pass


class ConsolePrinter(Printer):
    def print(self, book: Book, strategy: DisplayStrategy) -> None:
        print(f"Printing the book: {book.title}...")
        print(strategy.render(book))


class ReversePrinter(Printer):
    def print(self, book: Book, strategy: DisplayStrategy) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(strategy.render(book))
