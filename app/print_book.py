from abc import ABC, abstractmethod

from app.book import Book


class Print(ABC):
    def __init__(self, book: Book) -> None:
        self._book = book

    @abstractmethod
    def print(self) -> None:
        pass


class PrintConsole(Print):
    def print(self) -> None:
        print(f"Printing the book: {self._book.title}...")
        print(self._book.content)


class PrintReverse(Print):
    def print(self) -> None:
        print(f"Printing the book in reverse: {self._book.title}...")
        print(self._book.content[::-1])
