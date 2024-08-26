from abc import ABC, abstractmethod

from app.book import Book


class Print(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class ConsolePrinter(Print):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReverseConsolePrinter(Print):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
