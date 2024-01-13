from abc import ABC, abstractmethod

from app.books import Book


class PrintService(ABC):
    @abstractmethod
    def print(self) -> None:
        pass


class ConsolePrintService(PrintService):
    def __init__(self, book: Book):
        self.book = book

    def print(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class ReversePrintService(PrintService):
    def __init__(self, book: Book) -> None:
        self.book = book

    def print(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])
