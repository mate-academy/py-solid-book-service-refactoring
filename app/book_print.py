from abc import ABC, abstractmethod

from app.book import Book


class PrintBook(ABC):

    @abstractmethod
    def print_book(self) -> None:
        pass


class ConsolePrintBook(PrintBook):

    def __init__(self, book: Book) -> None:
        self._book = book

    def print_book(self) -> None:
        print(f"Printing the book: {self._book.title}")
        print(self._book.content)


class ReversePrintBook(PrintBook):

    def __init__(self, book: Book) -> None:
        self._book = book

    def print_book(self) -> None:
        print(f"Printing the book (reversed): {self._book.title}")
        print(self._book.content[::-1])
