from abc import ABC, abstractmethod

from app.book import Book


class Printer(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrint(Printer):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(Printer):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
