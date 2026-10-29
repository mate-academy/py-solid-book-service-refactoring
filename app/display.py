from abc import ABC, abstractmethod

from app.book import Book


class DisplayBook(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(DisplayBook):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayBook):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
