from abc import ABC, abstractmethod

from app.books import Book


class Displayer(ABC):
    @abstractmethod
    def run(self, book: Book) -> None:
        pass


class ConsoleDisplayer(Displayer):
    def run(self, book: Book) -> None:
        print(book.content)


class ReverseDisplayer(Displayer):
    def run(self, book: Book) -> None:
        print(book.content[::-1])
