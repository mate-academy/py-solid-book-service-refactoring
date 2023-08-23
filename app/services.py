from abc import ABC, abstractmethod

from app.book import Book


class BaseDisplay(ABC):
    @staticmethod
    @abstractmethod
    def display(book: Book) -> None:
        pass


class ConsoleDisplay(BaseDisplay):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content)


class ReverseDisplay(BaseDisplay):
    @staticmethod
    def display(book: Book) -> None:
        print(book.content[::-1])


class BasePrintBook(ABC):
    @staticmethod
    @abstractmethod
    def book_printing(book: Book) -> None:
        pass


class PrintBookConsole(BasePrintBook):
    @staticmethod
    def book_printing(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintBookReverse(BasePrintBook):
    @staticmethod
    def book_printing(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
