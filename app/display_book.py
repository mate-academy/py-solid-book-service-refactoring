from app.book import Book
from abc import ABC, abstractmethod


class Displayer(ABC):
    @abstractmethod
    def display(self) -> None:
        pass


class BookConsoleDisplayer(Displayer):
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self) -> None:
        print(self.book.content)


class BookReverseDisplayer(Displayer):
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self) -> None:
        print(self.book.content[::-1])
