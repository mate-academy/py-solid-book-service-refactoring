from abc import ABC, abstractmethod

from app.books import Book


class DisplayService(ABC):
    @abstractmethod
    def display(self) -> None:
        pass


class ConsoleDisplayService(DisplayService):
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self) -> None:
        print(self.book.content)


class ReverseDisplayService(DisplayService):
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self):
        print(self.book.content[::-1])
