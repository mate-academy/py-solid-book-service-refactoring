from abc import ABC, abstractmethod
from app.book import Book


class BookDisplay(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def display(self) -> None:
        ...


class ConsoleDisplay(BookDisplay):
    def display(self) -> None:
        print(self.book.content)


class ReverseDisplay(BookDisplay):
    def display(self) -> None:
        print(self.book.content[::-1])
