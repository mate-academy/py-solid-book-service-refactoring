from printer.base import Printer
from models.book import Book


class PrintConsole(Printer):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)
