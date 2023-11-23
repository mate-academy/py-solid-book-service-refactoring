from abc import ABC, abstractmethod

from app.book import Book


class Display(ABC):
    def __init__(self, book: Book):
        self.book = book

    @abstractmethod
    def display(self) -> None:
        pass


class ConsoleDisplay(Display):
    def display(self) -> None:
        print(self.book.content)


class ReverseConsoleDisplay(Display):
    def display(self) -> None:
        print(self.book.content[::-1])
