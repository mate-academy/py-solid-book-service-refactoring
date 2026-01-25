from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Dict

if TYPE_CHECKING:  # only for type hints, no runtime import
    from app.main import Book


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: "Book") -> None:
        ...


class ConsoleDisplayStrategy(DisplayStrategy):
    def display(self, book: "Book") -> None:
        print(book.content)


class ReverseDisplayStrategy(DisplayStrategy):
    def display(self, book: "Book") -> None:
        print(book.content[::-1])


class BookDisplayer:
    """Service responsible only for how the book is displayed."""

    def __init__(self) -> None:
        self._strategies: Dict[str, DisplayStrategy] = {
            "console": ConsoleDisplayStrategy(),
            "reverse": ReverseDisplayStrategy(),
        }

    def display(self, book: "Book", display_type: str) -> None:
        strategy = self._strategies.get(display_type)
        if strategy is None:
            # Keep exactly the same error message as in original code
            raise ValueError(f"Unknown display type: {display_type}")
        strategy.display(book)
