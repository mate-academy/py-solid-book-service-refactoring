from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print_book(self, book) -> None:
        pass


class ConsolePrinter(Printer):
    def print_book(self, book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(Printer):
    def print_book(self, book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
