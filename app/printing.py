from abc import ABC, abstractmethod

from app.models import Book


class PrintProcessor(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class ConsolePrint(PrintProcessor):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(PrintProcessor):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
