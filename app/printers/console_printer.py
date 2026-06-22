from app.models.book import Book
from app.printers.base import Printer


class ConsolePrinter(Printer):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)
