from abc import ABC, abstractmethod

from app.book import Book


class Printer(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrinter(Printer):
    def print_book(self, book: Book) -> None:
        print(
            f"Printing the book: {book.title}...\n"
            f"{book.content}"
        )


class ReversePrinter(Printer):
    def print_book(self, book: Book) -> None:
        print(
            f"Printing the book in reverse: {book.title}...\n"
            f"{book.content[::-1]}"
        )
