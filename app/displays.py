from abc import ABC, abstractmethod

from app.books import Book


class BaseDisplay(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(BaseDisplay):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(BaseDisplay):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class Viewer:
    def __init__(self, displayer: BaseDisplay) -> None:
        self._displayer = displayer

    def display(self, book: Book) -> None:
        self._displayer.display(book)
