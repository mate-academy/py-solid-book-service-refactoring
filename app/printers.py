from typing import Protocol

from app.models import Book


class BookPrinter(Protocol):
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrinter:
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter:
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


PRINTERS: dict[str, BookPrinter] = {
    "console": ConsolePrinter(),
    "reverse": ReversePrinter(),
}
