from abc import ABC, abstractmethod
from app.book import Book


class Display(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(Display):
    def display(self, book: Book) -> None:
        print(book)


class ReverseDisplay(Display):
    def display(self, book: Book) -> None:
        reversed_book = Book(book.title[::-1], book.content[::-1])
        print(reversed_book)
