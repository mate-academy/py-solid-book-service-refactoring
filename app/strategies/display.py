from abc import ABC, abstractmethod

from app.models.book import Book


class IDisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(IDisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(IDisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
