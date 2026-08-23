from app.book import Book

from app.printing.base import Printer


class ReversePrinter(Printer):
    def print_book(self, book: "Book") -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
