from abc import ABC, abstractmethod

from app.book import Book


class BookPrinter(ABC):
    @staticmethod
    @abstractmethod
    def print(book: Book) -> None:
        pass


class BookPrinterConsole(BookPrinter):
    @staticmethod
    def print(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class BookPrinterReverse(BookPrinter):
    @staticmethod
    def print(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
