from abc import ABC, abstractmethod

from app.book import Book


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


PRINT_STRATEGIES: dict[str, PrintStrategy] = {
    "console": ConsolePrint(),
    "reverse": ReversePrint(),
}


def print_book(book: Book, print_type: str) -> None:
    strategy = PRINT_STRATEGIES.get(print_type)
    if strategy is None:
        raise ValueError(f"Unknown print type: {print_type}")
    strategy.print_book(book)
