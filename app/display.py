from app.model import Book
from abc import ABC, abstractmethod


class DisplayBook(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class DisplayConsole(DisplayBook):
    def display(self, book: Book) -> None:
        print(book.content)


class DisplayReverse(DisplayBook):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
