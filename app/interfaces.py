from typing import Protocol

from app.models import Book


class Displayer(Protocol):
    def display(self, book: Book) -> None:
        ...


class Printer(Protocol):
    def print_book(self, book: Book) -> None:
        ...


class Serializer(Protocol):
    def serialize(self, book: Book) -> str:
        ...
