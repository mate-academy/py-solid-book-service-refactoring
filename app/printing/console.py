from app.book import Book
from app.printing.base import Printer


class ConsolePrinter(Printer):
    def print_book(self, book: "Book") -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)
