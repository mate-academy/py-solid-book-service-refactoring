from abc import ABC, abstractmethod

from app.book import Book


class Printer(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrinter(Printer):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(Printer):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


PRINTERS: dict[str, Printer] = {
    "console": ConsolePrinter(),
    "reverse": ReversePrinter(),
}


def get_printer(print_type: str) -> Printer:
    printer = PRINTERS.get(print_type)
    if printer is None:
        raise ValueError(f"Unknown print type: {print_type}")
    return printer
