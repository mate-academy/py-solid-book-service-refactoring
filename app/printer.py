from abc import ABC, abstractmethod

from app.models import Book
from app.display import DisplayStrategy


class PrintStrategy(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class ConsolePrinter(PrintStrategy):
    def __init__(self, display_strategy: DisplayStrategy) -> None:
        self.display_strategy = display_strategy

    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        self.display_strategy.display(book)


class ReversePrinter(PrintStrategy):
    def __init__(self, display_strategy: DisplayStrategy) -> None:
        self.display_strategy = display_strategy

    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        self.display_strategy.display(book)
