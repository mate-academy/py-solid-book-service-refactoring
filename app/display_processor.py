from abc import ABC, abstractmethod

from app.book import Book


class DisplayProcessor(ABC):
    @abstractmethod
    def display(self) -> None:
        pass


class DisplayConsoleProcessor(DisplayProcessor):
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self) -> None:
        print(self.book.content)


class DisplayReverseProcessor(DisplayProcessor):
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self) -> None:
        print(self.book.content[::-1])
