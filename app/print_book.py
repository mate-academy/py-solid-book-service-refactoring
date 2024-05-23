from abc import ABC, abstractmethod
from app.book import Book


class AbstractBookPrint(ABC):

    @abstractmethod
    def print_book(self) -> None:
        pass


class PrintConsole(AbstractBookPrint):
    def __init__(self, book: Book) -> None:
        self.book = book

    def print_book(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class PrintReverse(AbstractBookPrint):
    def __init__(self, book: Book) -> None:
        self.book = book

    def print_book(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])
