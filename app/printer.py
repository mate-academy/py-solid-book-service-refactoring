from abc import ABC

from app.book import Book


class Printer(ABC):

    @staticmethod
    def print(book: Book) -> None:
        pass


class ConsolePrinter(Printer):
    @staticmethod
    def print(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(Printer):
    @staticmethod
    def print(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
