from abc import ABC, abstractmethod
from app.models import Book


class BookDisplayer(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplayer(BookDisplayer):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayer(BookDisplayer):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
