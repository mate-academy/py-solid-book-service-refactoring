from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from .book import Book


class PrintStrategy(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        raise NotImplementedError


class ConsolePrint(PrintStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(PrintStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class PrintService:
    _strategies: Dict[str, PrintStrategy] = {
        "console": ConsolePrint(),
        "reverse": ReversePrint(),
    }

    @classmethod
    def print_book(cls, book: Book, print_type: str) -> None:
        strategy = cls._strategies.get(print_type)
        if strategy is None:
            raise ValueError(f"Unknown print type: {print_type}")
        strategy.print_book(book)
