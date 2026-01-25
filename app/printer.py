from __future__ import annotations

from typing import Protocol


class BookProtocol(Protocol):
    title: str
    content: str


class BookPrinter:
    """Handles printing book content."""

    def print_book(self, book: BookProtocol, print_type: str) -> None:
        if print_type == "console":
            self._print_console(book)
            return

        if print_type == "reverse":
            self._print_reverse(book)
            return

        raise ValueError(f"Unknown print type: {print_type}")

    def _print_console(self, book: BookProtocol) -> None:
        print(book.title)
        print(book.content)

    def _print_reverse(self, book: BookProtocol) -> None:
        print(book.title)
        print(book.content[::-1])
