from abc import ABC, abstractmethod

from app.book import Book


class Displayer(ABC):
    @abstractmethod
    def display(self) -> None:
        pass


class ConsoleDisplayer(Displayer):
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self) -> None:
        print(self.book.content)


class ReverseDisplayer(Displayer):
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self) -> None:
        print(self.book.content[::-1])
