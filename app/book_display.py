from abc import ABC, abstractmethod

from app.book import Book


class DisplayBook(ABC):

    @abstractmethod
    def display(self) -> None:
        pass


class ConsoleDisplayBook(DisplayBook):

    def __init__(self, book: Book) -> None:
        self._book = book

    def display(self) -> None:
        print(self._book.content)


class ReverseDisplayBook(DisplayBook):

    def __init__(self, book: Book) -> None:
        self._book = book

    def display(self) -> None:
        print(self._book.content[::-1])
