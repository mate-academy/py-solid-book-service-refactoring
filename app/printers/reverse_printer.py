from app.models.book import Book
from app.printers.base import Printer


class ReversePrinter(Printer):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
