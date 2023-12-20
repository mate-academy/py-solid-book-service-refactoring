from abc import ABC, abstractmethod
from app.book import Book


class Display(ABC):
    @abstractmethod
    def display_content(self, book: Book) -> None:
        pass


class ConsoleDisplay(Display):
    def display_content(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(Display):
    def display_content(self, book: Book) -> None:
        print(book.content[::-1])
