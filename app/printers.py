from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print_book(self, title: str, content: str) -> None:
        pass


class ConsolePrinter(Printer):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book: {title}...\n{content}")


class ReversePrinter(Printer):
    def print_book(self, title: str, content: str) -> None:
        print(f"Printing the book in reverse: {title}...\n{content[::-1]}")