from abc import ABC, abstractmethod
from app.book import Book


class AbstractBookDisplay(ABC):

    @abstractmethod
    def display(self) -> None:
        pass


class DisplayConsole(AbstractBookDisplay):
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self) -> None:
        print(self.book.content)


class DisplayReverse(AbstractBookDisplay):
    def __init__(self, book: Book) -> None:
        self.book = book

    def display(self) -> None:
        print(self.book.content[::-1])
