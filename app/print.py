from app.models import Book
from app.interface import DisplayInterface


class PrintConsole(DisplayInterface):
    def display(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverse(DisplayInterface):
    def display(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
