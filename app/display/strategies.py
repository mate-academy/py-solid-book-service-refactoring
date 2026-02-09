from app.display.base import DisplayBook
from app.models import Book


class ConsoleDisplay(DisplayBook):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayBook):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
