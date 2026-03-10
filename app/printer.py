from abc import ABC, abstractmethod
from .book import Book


class PrintStrategy(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrinter(PrintStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(PrintStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


PRINT_STRATEGIES = {
    "console": ConsolePrinter(),
    "reverse": ReversePrinter(),
}


def print_book(book: Book, print_type: str) -> None:
    if print_type not in PRINT_STRATEGIES:
        raise ValueError(f"Unknown print type: {print_type}")
    PRINT_STRATEGIES[print_type].print_book(book)
