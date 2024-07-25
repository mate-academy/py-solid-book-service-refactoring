from abc import ABC, abstractmethod

from app.book import Book


class Displayer(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplayer(Displayer):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayer(Displayer):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
