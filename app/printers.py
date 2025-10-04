from abc import ABC, abstractmethod

from app.books import Book


class Printer(ABC):

    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class ConsolePrinter(Printer):

    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(Printer):

    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class BookPrinter:

    def __init__(self, printer: Printer) -> None:
        self.printer = printer

    def print_book(self, book: Book) -> None:
        self.printer.print(book)
