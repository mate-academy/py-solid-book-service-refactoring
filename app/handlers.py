from app.book import Book
from app.strategies import (
    SERIALIZATION_STRATEGIES,
    PRINT_STRATEGIES,
    DISPLAY_STRATEGIES,
)


def handle_display(book: Book, method_type: str) -> None:
    strategy = DISPLAY_STRATEGIES.get(method_type)
    if strategy is None:
        raise ValueError(f"Unknown display strategy: {method_type}")
    strategy.display(book)


def handle_print(book: Book, method_type: str) -> None:
    strategy = PRINT_STRATEGIES.get(method_type)
    if strategy is None:
        raise ValueError(f"Unknown print strategy: {method_type}")
    strategy.print_book(book)


def handle_serialize(book: Book, method_type: str) -> str | None:
    strategy = SERIALIZATION_STRATEGIES.get(method_type)
    if strategy is None:
        raise ValueError(f"Unknown serialization strategy: {method_type}")
    return strategy.serialize(book)
