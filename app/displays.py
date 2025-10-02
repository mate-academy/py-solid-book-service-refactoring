from abc import ABC, abstractmethod

from app.models import Book


class IDisplay(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(IDisplay):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(IDisplay):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class ConsolePrinter(IDisplay):
    def display(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(IDisplay):
    def display(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
