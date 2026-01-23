from typing import Any

from app.abstract_models import Print


class ConsolePrint(Print):
    def print(self, book: Any) -> None:
        print(f"Printing the book: {book.title}...\n{book.content}")


class ReversedPrint(Print):
    def print(self, book: Any) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content[::-1])
