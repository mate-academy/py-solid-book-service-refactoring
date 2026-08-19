from abc import ABC, abstractmethod

from app.book import Book


class DisplayBase(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(DisplayBase):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayBase):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
