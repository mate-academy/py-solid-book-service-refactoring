from abc import ABC, abstractmethod

from app.book import Book


class BookPrinter(ABC):
    @staticmethod
    @abstractmethod
    def print(book: Book) -> None:
        pass


class BookConsolePrinter(BookPrinter):
    @staticmethod
    def print(book: Book) -> str:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class BookReversePrinter(BookPrinter):
    @staticmethod
    def print(book: Book) -> str:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
