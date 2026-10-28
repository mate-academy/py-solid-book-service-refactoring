from abc import ABC, abstractmethod

from app.models import Book


class Displayer(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class BookDisplayConsole(Displayer):
    def display(self, book: Book) -> None:
        print(book.content)


class BookDisplayReverse(Displayer):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
