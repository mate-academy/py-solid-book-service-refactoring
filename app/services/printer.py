from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.book import Book

class BookConsoleDisplayer:
    @staticmethod
    def display(book: Book, method_type: str) -> None:
        print(f"Displaying book {book.title} using {method_type}")

class BookPrinter:
    @staticmethod
    def print_book(book: Book, method_type: str) -> None:
        print(f"Printing book {book.title} using {method_type}")

