from abc import ABC, abstractmethod

from app.book import Book


class BookPrint(ABC):
    @staticmethod
    @abstractmethod
    def print_book(book: Book) -> None:
        pass


class ConsolePrint(BookPrint):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReverserPrint(BookPrint):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
