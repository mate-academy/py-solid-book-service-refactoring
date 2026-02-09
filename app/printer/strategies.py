from app.printer.base import PrintBook
from app.models import Book


class ConsolePrint(PrintBook):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...\n"
              f"{book.content}")


class ReversePrint(PrintBook):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...\n"
              f"{book.content[::-1]}")
