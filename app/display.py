from abc import ABC, abstractmethod

from app.models import Book


class DisplayStrategy(ABC):
    @abstractmethod
    def display_book(self, book: Book) -> None:
        pass


class ConsoleDisplay(DisplayStrategy):
    def display_book(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    def display_book(self, book: Book) -> None:
        print(book.content[::-1])
