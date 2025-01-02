from abc import ABC, abstractmethod

from app.books import Book


class Printer(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrinter(Printer):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}... {book.content}")


class ReversePrinter(Printer):
    def print_book(self, book: Book) -> None:
        print(f"Book in reverse  {book.title}... {book.content[::-1]}")
