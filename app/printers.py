from abc import ABC, abstractmethod
from app.books import Book


class Printer(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class ConsolePrinter:
    @staticmethod
    def print(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter:
    @staticmethod
    def print(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
