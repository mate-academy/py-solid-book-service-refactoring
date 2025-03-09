from abc import ABC, abstractmethod

from app.book import Book


class DisplayInterface(ABC):
    @abstractmethod
    def execute(self, book: Book) -> None:
        pass


class ConsoleDisplay(DisplayInterface):
    def execute(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayInterface):
    def execute(self, book: Book) -> None:
        print(book.content[::-1])
