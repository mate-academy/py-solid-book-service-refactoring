from abc import ABC, abstractmethod

from app.book import Book


class Display(ABC):
    @abstractmethod
    def display(self, book: "Book") -> None:
        pass


class ConsoleDisplay(Display):
    def display(self, book: "Book") -> None:
        print(book.content)


class ReverseDisplay(Display):
    def display(self, book: "Book") -> None:
        print(book.content[::-1])
