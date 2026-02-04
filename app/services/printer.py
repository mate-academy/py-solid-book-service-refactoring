from abc import ABC, abstractmethod

from app.book import Book


class Printer(ABC):
    @abstractmethod
    def execute(self, book: Book) -> None:
        pass


class ConsolePrinter(Printer):
    def execute(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(Printer):
    def execute(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
