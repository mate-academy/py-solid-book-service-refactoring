from app.contracts import BookProtocol
from app.printing.base import Printer


class ReversePrinter(Printer):
    def print(self, book: BookProtocol) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
