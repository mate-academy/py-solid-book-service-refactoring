from __future__ import annotations

from typing import Dict, Protocol


class BookProtocol(Protocol):
    title: str
    content: str


class PrintStrategy(Protocol):
    def print_book(self, book: BookProtocol) -> None:
        ...


class ConsolePrinter:
    def print_book(self, book: BookProtocol) -> None:
        print(book.title)
        print(book.content)


class ReversePrinter:
    def print_book(self, book: BookProtocol) -> None:
        print(book.title)
        print(book.content[::-1])


class BookPrinter:
    """Prints a book using registered strategies."""

    def __init__(
        self,
        strategies: Dict[str, PrintStrategy] | None = None,
    ) -> None:
        self._strategies: Dict[str, PrintStrategy] = (
            strategies
            if strategies is not None
            else {
                "console": ConsolePrinter(),
                "reverse": ReversePrinter(),
            }
        )

    def print_book(self, book: BookProtocol, print_type: str) -> None:
        if print_type not in self._strategies:
            raise ValueError(f"Unknown print type: {print_type}")

        strategy = self._strategies[print_type]
        strategy.print_book(book)
