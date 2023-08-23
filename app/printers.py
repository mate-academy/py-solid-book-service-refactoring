from abc import abstractmethod

from app.book import Book
from app.displays import ConsoleDisplay, ReverseDisplay


class Printer:
    @abstractmethod
    def perform_print(self, book: Book) -> None:
        pass


class ConsolePrinter(Printer):
    def perform_print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        ConsoleDisplay().perform_display(book)


class ReversePrinter(Printer):
    def perform_print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        ReverseDisplay().perform_display(book)
