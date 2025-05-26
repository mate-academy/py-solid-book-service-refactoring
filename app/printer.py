from abc import ABC, abstractmethod

from app.book import Book


class IBookPrinter(ABC):
    def __init__(self, book: Book) -> None:
        self.book = book

    @abstractmethod
    def print(self) -> None:
        pass


class ConsoleBookPrinter(IBookPrinter):
    def print(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class ReverseBookPrinter(IBookPrinter):
    def print(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])


def select_printer(method_type: str) -> type[IBookPrinter]:
    printers = {
        "console": ConsoleBookPrinter,
        "reverse": ReverseBookPrinter,
    }

    return printers[method_type]
