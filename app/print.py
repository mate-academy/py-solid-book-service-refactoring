from abc import ABC, abstractmethod

from app.book import Book


class Print(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def print(self, message: str) -> None:
        pass


class ConsolePrint(Print):
    def print(self, message: str) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class ReversePrint(Print):
    def print(self, message: str) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])
