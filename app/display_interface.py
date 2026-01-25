from abc import ABC, abstractmethod

from app.model import Book


class DisplayStrategy(ABC):
    @abstractmethod
    def execute(self, book: Book) -> None:
        pass


class ConsoleDisplay(DisplayStrategy):
    def execute(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    def execute(self, book: Book) -> None:
        print(book.content[::-1])
