from abc import ABC, abstractmethod

from app.book import Book


class BookDisplay(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleBookDisplay(BookDisplay):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseBookDisplay(BookDisplay):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
