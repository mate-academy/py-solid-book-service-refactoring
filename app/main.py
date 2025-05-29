from __future__ import annotations

from app.book import Book
from app.interfaces import (
    IDisplayStrategy,
    IPrintStrategy,
    ISerializationStrategy,
)
from app.display_strategies import (
    ConsoleDisplayStrategy,
    ReverseDisplayStrategy,
)
from app.print_strategies import ConsolePrintStrategy, ReversePrintStrategy
from app.serialization_strategies import JsonSerializer, XmlSerializer

DISPLAY_STRATEGIES: dict[str, IDisplayStrategy] = {
    "console": ConsoleDisplayStrategy(),
    "reverse": ReverseDisplayStrategy(),
}

PRINT_STRATEGIES: dict[str, IPrintStrategy] = {
    "console": ConsolePrintStrategy(ConsoleDisplayStrategy()),
    "reverse": ReversePrintStrategy(ReverseDisplayStrategy()),
}

SERIALIZATION_STRATEGIES: dict[str, ISerializationStrategy] = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    result = None
    for cmd, method_type in commands:
        if cmd == "display":
            strategy = DISPLAY_STRATEGIES.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown display type: {method_type}")
            strategy.display(book.content)
        elif cmd == "print":
            strategy = PRINT_STRATEGIES.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown print type: {method_type}")
            strategy.print_book(book.title, book.content)
        elif cmd == "serialize":
            strategy = SERIALIZATION_STRATEGIES.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown serialize type: {method_type}")
            result = strategy.serialize(book.get_data())
            return result
        else:
            raise ValueError(f"Unknown command: {cmd}")

    return result
