from app.contracts import BookProtocol
from app.printing.base import Printer


class ConsolePrinter(Printer):
    def print(self, book: BookProtocol) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)
