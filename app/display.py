from typing import Protocol
from app.models import Book


class DisplayStrategy(Protocol):
    def display(self, book: Book) -> None:
        ...


class ConsoleDisplay:
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay:
    def display(self, book: Book) -> None:
        print(book.content[::-1])
