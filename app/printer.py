from abc import ABC, abstractmethod

from app.book import Book


class PrinterBook(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def print_book(self) -> None:
        pass


class ConsolePrinterBook(PrinterBook):
    def print_book(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)


class ReversePrinterBook(PrinterBook):
    def print_book(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])
