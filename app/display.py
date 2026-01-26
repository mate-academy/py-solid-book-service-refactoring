from app.models import Book
from app.interface import DisplayInterface


class ConsoleDisplay(DisplayInterface):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayInterface):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
