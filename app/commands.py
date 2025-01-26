from app.book import Book
from app.strategies import (
    DisplayStrategy,
    Console,
    Reverse,
    SerializationStrategy,
)


class Display:
    def __init__(self, strategy: DisplayStrategy) -> None:
        self.strategy = strategy

    def action(self, book: Book) -> None:
        self.strategy.display(book)


class PrintBook:
    def __init__(self, strategy: DisplayStrategy) -> None:
        self.strategy = strategy

    def action(self, book: Book) -> None:
        if isinstance(self.strategy, Console):
            print(f"Printing the book: {book.title}...")
        elif isinstance(self.strategy, Reverse):
            print(f"Printing the book in reverse: {book.title}...")
        self.strategy.display(book)


class Serializer:
    def __init__(self, strategy: SerializationStrategy) -> None:
        self.strategy = strategy

    def action(self, book: Book) -> str:
        return self.strategy.serialize(book)
