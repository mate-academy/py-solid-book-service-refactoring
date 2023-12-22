from abc import ABC, abstractmethod
from app.book_implementation import Book


class Printer(ABC):
    @staticmethod
    @abstractmethod
    def print_book(book: Book) -> None:
        pass


class ConsolePrint(Printer):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(Printer):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
