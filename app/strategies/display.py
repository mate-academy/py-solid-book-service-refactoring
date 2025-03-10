from abc import ABC, abstractmethod

from app.book import Book


class BookDisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleBookDisplayStrategy(BookDisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseBookDisplayStrategy(BookDisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
