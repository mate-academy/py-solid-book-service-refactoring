from abc import ABC, abstractmethod

from app.book import Book


class BookPrint(ABC):
    @staticmethod
    @abstractmethod
    def print(book: Book) -> None:
        pass


class BookPrintConsole(BookPrint):
    @staticmethod
    def print(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class BookPrintReverse(BookPrint):
    @staticmethod
    def print(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
