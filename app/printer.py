from abc import ABC, abstractmethod
from app.models import Book


class Printer(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class ConsolePrint(Printer):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(Printer):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


def get_printer(print_type: str) -> Printer:
    if print_type == "console":
        return ConsolePrint()
    elif print_type == "reverse":
        return ReversePrint()
    else:
        raise ValueError(f"Unknown print type: {print_type}")
