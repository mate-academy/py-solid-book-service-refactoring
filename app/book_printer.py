from abc import ABC, abstractmethod
from app.book import Book


class BookPrinter(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class BookPrinterConsole(BookPrinter):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class BookPrinterReverse(BookPrinter):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class Printer:
    printers = {"console": BookPrinterConsole, "reverse": BookPrinterReverse}

    def go_print(self, print_type: str, book: Book) -> str:
        if print_type in self.printers:
            return self.printers[print_type]().print(book)
        raise ValueError(f"Unknown print type: {print_type}")
