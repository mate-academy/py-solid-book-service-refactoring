from abc import ABC, abstractmethod

from app.book import Book


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


DISPLAY_STRATEGIES: dict[str, DisplayStrategy] = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}


def display_book(book: Book, display_type: str) -> None:
    strategy = DISPLAY_STRATEGIES.get(display_type)
    if strategy is None:
        raise ValueError(f"Unknown display type: {display_type}")
    strategy.display(book)
