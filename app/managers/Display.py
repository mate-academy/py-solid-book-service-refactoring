from abc import ABC, abstractmethod
from app.managers import Book


class DisplayBasic(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class DisplayConsole(DisplayBasic):
    def display(self, book: Book) -> None:
        print(book.content)


class DisplayReverse(DisplayBasic):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
