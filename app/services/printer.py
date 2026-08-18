from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.book import Book

class BookConsoleDisplayer:
    @staticmethod
    def display(book: Book, method_type: str) -> None:
        book.display(method_type)

class BookPrinter:
    @staticmethod
    def print_book(book: Book, method_type: str) -> None:
        book.print_book(method_type)

