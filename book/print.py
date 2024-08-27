from abc import (
    ABC,
    abstractmethod
)

from book.book import Book


class Print(ABC):
    @abstractmethod
    def print(self, book: Book) -> None:
        pass


class PrintConsole(Print):
    def print(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class PrintReverse(Print):
    def print(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class PrintBook:
    _strategies = {
        "console": PrintConsole(),
        "reverse": PrintReverse(),
    }

    @staticmethod
    def print(book: Book, print_type: str) -> None:
        print_strategy = PrintBook._strategies.get(print_type)
        if print_strategy is None:
            raise ValueError(f"Unknown display type: {print_type}")
        return print_strategy.print(book)
