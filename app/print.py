from app.book import Book
from abc import ABC, abstractmethod


class Print(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class ConsolePrint(Print):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}", book.content)


class ReversePrint(Print):
    def print(self, book: Book) -> None:
        print(f"Reversing book: {book.title}", book.content[::-1])
