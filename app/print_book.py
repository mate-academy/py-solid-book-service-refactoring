from abc import ABC, abstractmethod

from app.book import Book


class PrintBook(ABC):
    @staticmethod
    @abstractmethod
    def print_book(book: Book) -> None:
        pass


class ConsolePrint(PrintBook):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(PrintBook):
    @staticmethod
    def print_book(book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


def print_book(book: Book, method_type: str) -> None:
    if method_type == "console":
        ConsolePrint.print_book(book)
    elif method_type == "reverse":
        ReversePrint.print_book(book)
    else:
        raise ValueError(f"Unknown print type: {method_type}")
