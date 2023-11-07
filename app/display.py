from abc import ABC

from app.book import Book


class Display(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self: Book) -> None:
        pass


class ConsoleDisplay(Display):
    def display(self: Book) -> None:
        print(self.content)


class ReverseDisplay(Display):
    def display(self: Book) -> None:
        print(self.content[::-1])
