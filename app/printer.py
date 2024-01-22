from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print(self, book: object) -> None:
        pass


class ConsolePrinter(Printer):
    def print(self, book: object) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(Printer):
    def print(self, book: object) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
