from abc import ABC, abstractmethod

from app.book import IBook


class IPrinter(ABC):
    @abstractmethod
    def print_book(self, book: IBook) -> None:
        pass


class ConsolePrinter(IPrinter):
    def print_book(self, book: IBook) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ConsoleReversePrinter(IPrinter):
    def print_book(self, book: IBook) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
