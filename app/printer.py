from abc import ABC, abstractmethod
from .book import Book


class BookPrinter(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrinter(BookPrinter):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(BookPrinter):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class PrinterFactory:
    @staticmethod
    def create_printer(print_type: str) -> BookPrinter:
        if print_type == "console":
            return ConsolePrinter()
        elif print_type == "reverse":
            return ReversePrinter()
        else:
            raise ValueError(f"Unknown print type: {print_type}")
