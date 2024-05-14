from abc import ABC, abstractmethod

from app.book import Book


class Printer(ABC):
    @staticmethod
    @abstractmethod
    def display(book: Book) -> None:
        pass


class PrinterConsole(Printer):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrinterReverse(Printer):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
