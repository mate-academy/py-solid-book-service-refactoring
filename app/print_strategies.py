from __future__ import annotations
from interfaces import PrintStrategy, BookDTO


class ConsolePrinter(PrintStrategy):
    def print_book(self, book: BookDTO) -> None:
        # еквівалентно старому print_book("console")
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(PrintStrategy):
    def print_book(self, book: BookDTO) -> None:
        # еквівалентно старому print_book("reverse")
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
