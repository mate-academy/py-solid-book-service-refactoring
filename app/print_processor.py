from abc import ABC, abstractmethod

from app.book import Book


class PrintProcessor(ABC):
    @staticmethod
    @abstractmethod
    def print(book: Book) -> None:
        pass


class PrintConsoleProcessor(PrintProcessor):
    @staticmethod
    def print(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverseProcessor(PrintProcessor):
    @staticmethod
    def print(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
