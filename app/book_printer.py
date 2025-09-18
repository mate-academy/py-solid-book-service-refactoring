from abc import ABC, abstractmethod

from .book import Book


class Printer(ABC):
    @staticmethod
    @abstractmethod
    def print_book(print_type: str) -> None:
        pass


class BookPrinterConsole(Printer):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book: {book.title}...\n{book.content}")


class BookPrinterReverse(Printer):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book: {book.title}...\n{book.content[::-1]}")
