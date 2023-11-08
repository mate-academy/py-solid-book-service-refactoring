from abc import ABC, abstractmethod

from app.book import Book


class PrintBook(ABC):
    def __init__(self, book: Book):
        self.book = book

    @abstractmethod
    def print_book(self) -> None:
        pass


class ConsolePrint(PrintBook):

    def print_book(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class ReversePrint(PrintBook):

    def print_book(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])


def print_book(book: Book, method_type: str) -> None:
    mappings = {"console": ConsolePrint, "reverse": ReversePrint}
    printer = mappings.get(method_type)
    if printer:
        printer(book).print_book()
    else:
        raise ValueError(f"Unknown print type: {method_type}")
