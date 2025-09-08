from printer.base import Printer
from models.book import Book


class PrintReverse(Printer):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
