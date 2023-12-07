from abc import ABC, abstractmethod

from . import BookABC


class Printer(ABC):
    @staticmethod
    @abstractmethod
    def print_book(book: BookABC) -> None:
        pass


class PrinterToConsole(Printer):
    @staticmethod
    def print_book(book: BookABC) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrinterInReverse(Printer):
    @staticmethod
    def print_book(book: BookABC) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
