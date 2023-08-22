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


class PrinterProceed:
    printers = {"console": ConsolePrinter, "reverse": ReversePrinter}

    def go_print(self, print_type: str, book: Book) -> str:
        if print_type in self.printers:
            return self.printers[print_type]().print_book(book)
        raise ValueError(f"Unknown print type: {print_type}")
