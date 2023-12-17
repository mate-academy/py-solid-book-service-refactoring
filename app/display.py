from abc import ABC, abstractmethod

from app.book import Book


class Display(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def display(self, message: str) -> None:
        pass


class ConsoleDisplay(Display):
    def display(self, message: str) -> None:
        print(self.book.content)


class ReverseDisplay(Display):
    def display(self, message: str) -> None:
        print(self.book.content[::-1])
