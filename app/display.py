from .book import Book
from abc import ABC, abstractmethod


class MethodType(ABC):
    @abstractmethod
    def console(self, book: Book) -> None:
        pass

    @abstractmethod
    def reverse(self, book: Book) -> None:
        pass


class BookDisplay(MethodType):
    def console(self, book: Book) -> None:
        print(book.content)

    def reverse(self, book: Book) -> None:
        print(book.content[::-1])
