from abc import ABC, abstractmethod
from app.book import Book

class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass

    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsoleDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)

    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])

    def print_book(self, book: Book) -> None:
        print(f"Printing the book in reverse: {book.title}...")
        print(book.content[::-1])


class DisplayManager:
    _strategies = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay()
    }

    @classmethod
    def get_strategy(cls, display_type: str) -> DisplayStrategy:
        if display_type not in cls._strategies:
            raise ValueError(f"Unknown display/print type: {display_type}")
        return cls._strategies[display_type]
