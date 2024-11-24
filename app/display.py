from abc import ABC, abstractmethod

from .book import Book


class Display(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(Display):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayer(Display):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
