from abc import ABC, abstractmethod

from app.book import Book


class IDisplayer(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplayer(IDisplayer):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayer(IDisplayer):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
