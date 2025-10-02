from abc import ABC, abstractmethod

from app.books import Book


class IDisplay(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class DisplayConsole(IDisplay):
    def display(self, book: Book) -> None:
        print(book.content)


class DisplayReverse(IDisplay):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
