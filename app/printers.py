from abc import ABC, abstractmethod

from app.book import Book


class PrintInterface(ABC):
    @abstractmethod
    def execute(self, book: Book) -> None:
        pass


class ConsolePrint(PrintInterface):
    def execute(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(PrintInterface):
    def execute(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
