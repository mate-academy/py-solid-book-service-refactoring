from abc import ABC, abstractmethod

from app.models import Book


class Printer(ABC):

    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrinter(Printer):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}")
        print(book.content)


class ReverseConsolePrinter(Printer):
    def print_book(self, book: Book) -> None:
        print(f"Printing the reversed book: {book.title}")
        print(book.content[::-1])
