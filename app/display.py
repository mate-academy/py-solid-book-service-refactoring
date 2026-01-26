from app.models import Book
from app.interface import DefaultInterface


class ConsoleDisplay(DefaultInterface):
    def run(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DefaultInterface):
    def run(self, book: Book) -> None:
        print(book.content[::-1])
