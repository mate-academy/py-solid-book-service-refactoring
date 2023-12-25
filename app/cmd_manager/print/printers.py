from abc import ABC, abstractclassmethod

from app.book import Book


class Printer(ABC):
    @staticmethod
    @abstractclassmethod
    def print_book(book: Book) -> None:
        pass


class ConsolePrinter(Printer):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(Printer):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
