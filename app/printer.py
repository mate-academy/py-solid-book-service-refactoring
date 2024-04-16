from abc import ABC, abstractmethod

from app.book import Book


class PrinterBehavior(ABC):

    @abstractmethod
    def print_book(self, book: Book) -> None:
        raise NotImplementedError


class ConsolePrinter(PrinterBehavior):

    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(PrinterBehavior):

    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


def create_printer_behavior(print_type: str) -> PrinterBehavior:
    if print_type == "console":
        return ConsolePrinter()
    elif print_type == "reverse":
        return ReversePrinter()
    raise ValueError(f"Unknown print type: {print_type}")
