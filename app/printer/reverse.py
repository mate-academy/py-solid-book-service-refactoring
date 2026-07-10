from app.book import Book
from app.printer.base import BasePrinter


class ReversePrinter(BasePrinter):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
