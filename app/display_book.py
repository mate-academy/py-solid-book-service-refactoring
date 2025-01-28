from abc import ABC, abstractmethod

from app.book import Book


class DisplayWay(ABC):
    @abstractmethod
    def display_book(self, book: Book) -> None:
        pass


class DisplayConsole(DisplayWay):
    def display_book(self, book: Book) -> None:
        print(book.content)


class DisplayReverse(DisplayWay):
    def display_book(self, book: Book) -> None:
        print(book.content[::-1])
