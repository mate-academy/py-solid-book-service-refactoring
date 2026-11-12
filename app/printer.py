from app.models import Book
from abc import ABC, abstractmethod


class BookPrinter(ABC):
    @abstractmethod
    def print_book(self, book: "Book") -> None:
        pass


class BookConsolePrinter(BookPrinter):
    def print_book(self, book: "Book") -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class BookReversePrinter(BookPrinter):
    def print_book(self, book: "Book") -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
