from abc import ABC, abstractmethod
from typing import Any


class PrintBook(ABC):
    @abstractmethod
    def print_type(self, book: Any) -> None:
        ...


class PrintConsole(PrintBook):
    def print_type(self, book: Any) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverse(PrintBook):
    def print_type(self, book: Any) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
