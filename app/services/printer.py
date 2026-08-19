from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.book import Book


class BookConsoleDisplayer:
    @staticmethod
    def display(book: Book, method_type: str) -> None:
        if method_type == "reverse":
            print(book.content[::-1])
        else:
            print(book.content)


class BookPrinter:
    @staticmethod
    def print_book(book: Book, method_type: str) -> None:
        print(book.title)
        if method_type == "reverse":
            print(book.content[::-1])
        else:
            print(book.content)
