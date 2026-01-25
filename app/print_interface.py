from abc import ABC, abstractmethod

from app.model import Book


class PrintStrategy(ABC):
    @abstractmethod
    def execute(self, book: Book) -> None:
        pass


class ConsolePrinter(PrintStrategy):
    def execute(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(PrintStrategy):
    def execute(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
