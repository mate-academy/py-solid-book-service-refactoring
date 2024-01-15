from abc import ABC, abstractmethod

from app.models import Book


class PrintBook(ABC):
    @staticmethod
    @abstractmethod
    def print_book(book: Book) -> None:
        pass


class PrintInConsole(PrintBook):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintToReversed(PrintBook):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
