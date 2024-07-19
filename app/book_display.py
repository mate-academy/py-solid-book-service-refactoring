from app.abstract_classes import IBookDisplay
from app.book_model import Book


class ConsoleBookDisplay(IBookDisplay):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseBookDisplay(IBookDisplay):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
