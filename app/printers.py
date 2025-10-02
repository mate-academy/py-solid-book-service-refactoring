from abc import ABC, abstractmethod

from .book import Book


class IPrint(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class ConsolePrint(IPrint):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(IPrint):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
