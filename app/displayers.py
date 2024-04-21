from abc import ABC, abstractmethod

from app.book import Book


class Displayer(ABC):

    @staticmethod
    @abstractmethod
    def display(book: Book) -> None:
        pass


class ConsoleDisplayer(Displayer):

    @staticmethod
    def display(book: Book) -> None:
        print(book.content)


class ReverseDisplayer(Displayer):

    @staticmethod
    def display(book: Book) -> None:
        print(book.content[::-1])
