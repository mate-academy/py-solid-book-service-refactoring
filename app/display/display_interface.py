from abc import ABC, abstractmethod

from app.book.book_model import Book


class DisplayInterface(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(DisplayInterface):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayInterface):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
