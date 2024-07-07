from abc import ABC, abstractmethod

from app.models import Book


class BookPrinter(ABC):
    @staticmethod
    @abstractmethod
    def print(book: Book) -> None:
        ...


class ConsoleBookPrinter(BookPrinter):
    @staticmethod
    def print(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReverseBookPrinter(BookPrinter):
    @staticmethod
    def print(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
