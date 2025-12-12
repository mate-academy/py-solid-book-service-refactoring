from .interfaces import IDisplay
from .models import Book


class ConsoleDisplay(IDisplay):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(IDisplay):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
