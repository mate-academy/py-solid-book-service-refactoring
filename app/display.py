from abc import ABC

from app.models import Book


class Display(ABC):
    pass


class BookDisplay(Display):
    def __init__(self, book: Book) -> None:
        self.book = book

    def console_display(self) -> None:
        print(self.book.content)

    def reverse_display(self) -> None:
        print(self.book.content[::-1])


class BookPrinter(Display):
    def __init__(self, book: Book) -> None:
        self.book = book

    def console_print(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)

    def reverse_print(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])
