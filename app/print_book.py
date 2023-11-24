from abc import ABC, abstractmethod
from app.book import Book


class PrintBook(ABC):
    @staticmethod
    @abstractmethod
    def print(book: Book) -> None:
        pass


class PrintBookInConsole(PrintBook):
    @staticmethod
    def print(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintBookInReverse(PrintBook):
    @staticmethod
    def print(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
