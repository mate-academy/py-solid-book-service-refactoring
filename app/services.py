from abc import ABC, abstractmethod

from app.models import Book


class IPrinter(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class IDisplayService(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class DisplayConsole(IDisplayService):
    def display(self, book: Book) -> None:
        print(book.content)


class DisplayReverse(IDisplayService):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class ConsolePrinter(IPrinter):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(IPrinter):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
