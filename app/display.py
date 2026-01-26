from __future__ import annotations
from abc import ABC, abstractmethod

from .book import Book


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


def get_display_strategy(display_type: str) -> DisplayStrategy:
    if display_type == "console":
        return ConsoleDisplay()
    if display_type == "reverse":
        return ReverseDisplay()
    raise ValueError(f"Unknown display type: {display_type}")
