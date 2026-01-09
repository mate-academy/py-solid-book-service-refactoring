from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.main import Book


class PrinterStrategy:
    def print_book(self, book: "Book") -> None:
        raise NotImplementedError


class ConsolePrinter(PrinterStrategy):
    def print_book(self, book: "Book") -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(PrinterStrategy):
    def print_book(self, book: "Book") -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
