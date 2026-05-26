from abc import ABC, abstractmethod

from app.books import Book


class BasePrint(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class ConsolePrint(BasePrint):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(BasePrint):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class Printer:
    def __init__(self, printer: BasePrint) -> None:
        self._printer = printer

    def print(self, book: Book) -> None:
        self._printer.print(book)
