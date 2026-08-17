from typing import Protocol
from app.models import Book


class PrintStrategy(Protocol):
    def print_book(self, book: Book) -> None:
        ...


class ConsolePrinter:
    def print_book(self, book: Book) -> None:
        print(f"{book.title}\n{book.content}")


class ReversePrinter:
    def print_book(self, book: Book) -> None:
        print(f"{book.title}\n{book.content[::-1]}")
