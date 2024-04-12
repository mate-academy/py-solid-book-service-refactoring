from abc import ABC, abstractmethod

from app.book import Book


class Printer(ABC):

    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class ConsolePrinter(Printer):

    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(Printer):

    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


def print_factor(book: Book, method_type: str) -> None:
    if method_type == "console":
        printer = ConsolePrinter()
        return printer.print(book)
    elif method_type == "reverse":
        printer = ReversePrinter()
        return printer.print(book)
    else:
        raise ValueError(f"Unknown print type: {method_type}")
