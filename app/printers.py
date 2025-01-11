from abc import ABC, abstractmethod

from app.book import Book


class Printer(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrinter(Printer):
    def __init__(self, print_type: str) -> None:
        self.print_type = print_type

    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(Printer):
    def __init__(self, print_type: str) -> None:
        self.print_type = print_type

    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


def choose_printer(print_type: str) -> Printer:
    if print_type == "console":
        return ConsolePrinter(print_type)
    elif print_type == "reverse":
        return ReversePrinter(print_type)
    else:
        raise ValueError(f"Unknown print type: {print_type}")
