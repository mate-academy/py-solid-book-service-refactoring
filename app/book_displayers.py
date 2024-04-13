from abc import ABC, abstractmethod

from app.book import Book


class BookDisplay(ABC):
    @abstractmethod
    def display(self) -> None:
        ...


class ConsoleDisplay(BookDisplay):
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self) -> None:
        print(self.book.content)


class ReverseDisplay(BookDisplay):
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self) -> None:
        print(self.book.content[::-1])
