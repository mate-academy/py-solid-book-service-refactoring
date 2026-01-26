from __future__ import annotations
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


def get_print_strategy(print_type: str) -> PrintStrategy:
    if print_type == "console":
        return ConsolePrinter()
    if print_type == "reverse":
        return ReversePrinter()
    raise ValueError(f"Unknown print type: {print_type}")
