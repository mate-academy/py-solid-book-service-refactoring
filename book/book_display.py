from abc import ABC, abstractmethod
from book.book import Book


class DisplayBook(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class DisplayBookConsole(DisplayBook):
    def display(self, book: Book) -> None:
        print(book.content)


class DisplayBookReverse(DisplayBook):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
