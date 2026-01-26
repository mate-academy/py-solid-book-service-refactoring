from app.models import Book
from app.interface import DefaultInterface


class PrintConsole(DefaultInterface):
    def run(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverse(DefaultInterface):
    def run(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
