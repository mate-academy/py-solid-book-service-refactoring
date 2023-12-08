from abc import ABC, abstractmethod

from app.book import Book


class Display(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def display(self) -> None:
        pass


class DisplayConsole(Display):
    def display(self) -> None:
        print(self.book.content)


class DisplayReverse(Display):
    def display(self) -> None:
        print(self.book.content[::-1])
