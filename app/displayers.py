from abc import ABC, abstractmethod

from app.book import Book


class BookDisplayer(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleBookDisplayer(BookDisplayer):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseBookDisplayer(BookDisplayer):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
