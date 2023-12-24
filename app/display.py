from abc import ABC, abstractmethod

from app.book import Book


class Display(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def display_book(self) -> None:
        pass


class ConsoleDisplay(Display):
    def display_book(self) -> None:
        print(self.book.content)


class ReverseDisplay(Display):
    def display_book(self) -> None:
        print(self.book.content[::-1])
