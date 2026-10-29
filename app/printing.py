
from abc import ABC, abstractmethod


class BookPrinter(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        pass


class ConsolePrinter(BookPrinter):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...")
        print(content)


class ReversePrinter(BookPrinter):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...")
        print(content[::-1])


PRINT_STRATEGIES = {
    "console": ConsolePrinter(),
    "reverse": ReversePrinter(),
}
