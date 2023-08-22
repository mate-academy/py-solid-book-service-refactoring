from abc import ABC, abstractmethod

from app.book import Book


class Printer(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass

    @staticmethod
    def get_printer_class(given_type: str) -> "Printer":
        if given_type == "console":
            return ConsolePrinter

        elif given_type == "reverse":
            return ReversedPrinter

        else:
            raise ValueError(f"Unknown print type: {given_type}")


class ConsolePrinter(Printer):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversedPrinter(Printer):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
