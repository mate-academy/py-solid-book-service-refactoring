from abc import ABC, abstractmethod
from app.interfaces import HasTitleContent


class PrintStrategy(ABC):
    @abstractmethod
    def print_book(self, book: HasTitleContent) -> None:
        pass


class ConsolePrinter(PrintStrategy):
    def print_book(self, book: HasTitleContent) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrinter(PrintStrategy):
    def print_book(self, book: HasTitleContent) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])
