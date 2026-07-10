from abc import ABC, abstractmethod

from app.book import Book


class DisplayType(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class DisplayConsole(DisplayType):
    def display(self, book: Book) -> None:
        print(book.content)


class DisplayReverse(DisplayType):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
