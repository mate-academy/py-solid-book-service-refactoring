from abc import ABC, abstractmethod

from app.book import Book


class Printer(ABC):

    @abstractmethod
    def printer(self) -> None:
        pass


class ConsolePrinter(Printer):

    def __init__(self, book: Book) -> None:
        self.title = book.title
        self.content = book.content

    def printer(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)


class ReversePrinter(Printer):

    def __init__(self, book: Book) -> None:
        self.title = book.title
        self.content = book.content

    def printer(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])
