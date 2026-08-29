"""Book printing abstractions and their concrete implementations."""

from abc import ABC, abstractmethod

from app.models import Book


class BookPrinter(ABC):
    """Define the interface implemented by every book printer."""

    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsoleBookPrinter(BookPrinter):
    """Print a book to the console in its original form."""

    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReverseBookPrinter(BookPrinter):
    """Print a book to the console with reversed content."""

    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
