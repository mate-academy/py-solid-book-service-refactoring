from abc import ABC, abstractmethod
from app.book import Book


class AbstractBookDisplay(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def display(self) -> None:
        pass


class DisplayConsole(AbstractBookDisplay):
    def display(self) -> None:
        print(self.book.content)


class DisplayReverse(AbstractBookDisplay):
    def display(self) -> None:
        print(self.book.content[::-1])
