from abc import ABC, abstractmethod

from app.book import Book


class Display(ABC):
    @abstractmethod
    def execute(self, book: Book) -> None:
        pass


class ConsoleDisplay(Display):
    def execute(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(Display):
    def execute(self, book: Book) -> None:
        print(book.content[::-1])
