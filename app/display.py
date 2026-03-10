from abc import ABC, abstractmethod
from .book import Book


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


DISPLAY_STRATEGIES = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}


def display_book(book: Book, display_type: str) -> None:
    if display_type not in DISPLAY_STRATEGIES:
        raise ValueError(f"Unknown display type: {display_type}")
    DISPLAY_STRATEGIES[display_type].display(book)
