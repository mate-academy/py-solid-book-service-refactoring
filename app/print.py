from abc import ABC, abstractmethod

from app.book import Book


class Print(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class ConsolePrint(Print):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(Print):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


def print_command(book: Book, method_type: str) -> None:
    if method_type == "console":
        method_type = ConsolePrint()
    elif method_type == "reverse":
        method_type = ReversePrint()
    else:
        raise ValueError(f"Unknown print type: {method_type}")
    method_type.print(book)
