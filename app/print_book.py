from abc import ABC, abstractmethod
from app.book import Book


class PrintBook(ABC):
    @staticmethod
    @abstractmethod
    def print_book(book: Book) -> None:
        pass


class PrintBookConsole(PrintBook):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintBookReverse(PrintBook):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
