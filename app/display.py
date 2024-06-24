from abc import ABC, abstractmethod

from app.book_model import Book


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
