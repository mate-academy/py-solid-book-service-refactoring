from abc import ABC, abstractmethod

from app.books import Book


class PrintStrategy(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrint(PrintStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(PrintStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


def get_print_strategy(print_type: str) -> PrintStrategy:
    if print_type == "console":
        return ConsolePrint()
    elif print_type == "reverse":
        return ReversePrint()
    else:
        raise ValueError(f"Unknown print type: {print_type}")
