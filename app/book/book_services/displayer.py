from abc import ABC, abstractmethod

from app.book.book import Book


class Displayer(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class DisplayerConsole(Displayer):
    def display(self, book: Book) -> None:
        print(book.content)


class DisplayerReverse(Displayer):
    def display(self, book: Book) -> None:
        print(book.content[::-1])
