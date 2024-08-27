from abc import ABC, abstractmethod

from app.book import Book


class Print(ABC):
    @abstractmethod
    def print(self, book: "Book") -> None:
        pass


class ConsolePrint(Print):
    def print(self, book: "Book") -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(Print):
    def print(self, book: "Book") -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
