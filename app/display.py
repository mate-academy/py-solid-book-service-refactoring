from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from .book import Book


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        raise NotImplementedError


class ConsoleDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class DisplayService:
    _strategies: Dict[str, DisplayStrategy] = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }

    @classmethod
    def display(cls, book: Book, display_type: str) -> None:
        strategy = cls._strategies.get(display_type)
        if strategy is None:
            raise ValueError(f"Unknown display type: {display_type}")
        strategy.display(book)
