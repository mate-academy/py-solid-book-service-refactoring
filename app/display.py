from abc import ABC, abstractmethod

from app.book import Book


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplayStrategy(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayStrategy(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
