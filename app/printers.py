from abc import ABC, abstractmethod

from app.books import Book


class IPrinter(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class PrintConsole(IPrinter):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverse(IPrinter):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
