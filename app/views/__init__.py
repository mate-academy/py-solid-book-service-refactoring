"""Concrete view implementations - following SRP and OCP.

Each view has a single responsibility and can be extended without
modifying existing code.
"""

from app.domain.book import Book
from app.interfaces import BookViewer, BookPrinter


class ConsoleBookViewer(BookViewer):
    """Display book content as-is to console."""

    def display(self, book: Book) -> None:
        print(book.content)


class ReverseBookViewer(BookViewer):
    """Display book content in reverse to console."""

    def display(self, book: Book) -> None:
        print(book.content[::-1])


class ConsoleBookPrinter(BookPrinter):
    """Print book content as-is to console with title."""

    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReverseBookPrinter(BookPrinter):
    """Print book content in reverse to console with title."""

    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
