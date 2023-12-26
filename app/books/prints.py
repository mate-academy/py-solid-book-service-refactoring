from abc import ABC, abstractmethod

from app.books.book import Book


class BookPrint(ABC):
    @staticmethod
    @abstractmethod
    def print(book: Book) -> None:
        pass


class ConsoleBookPrint(BookPrint):
    @staticmethod
    def print(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReverseBookPrint(BookPrint):
    @staticmethod
    def print(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
