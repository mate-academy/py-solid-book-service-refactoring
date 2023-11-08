from abc import ABC, abstractmethod

from app.books import Book


class Display(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def display(self: Book) -> None:
        pass


class ConsoleDisplay(Display):
    def display(self: Book) -> None:
        print(self.content)


class ReverseDisplay(Display):
    def display(self: Book) -> None:
        print(self.content[::-1])
