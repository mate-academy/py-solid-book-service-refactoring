from abc import ABC, abstractmethod

from app.book import Book


class PrintBook(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrintBook(PrintBook):
    def __init__(self, book: Book) -> None:
        self.title = book.title
        self.content = book.content

    def print_book(self) -> None:
        print(f"Printing the book: {self.title}...")
        print(self.content)


class ReversePrintBook(PrintBook):
    def __init__(self, book: Book) -> None:
        self.title = book.title
        self.content = book.content

    def print_book(self) -> None:
        print(f"Printing the book in reverse: {self.title}...")
        print(self.content[::-1])
