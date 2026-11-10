from __future__ import annotations
from app.models.book import Book
from app.services.printer import (
    ConsoleDisplay,
    ReverseDisplay,
    ConsolePrinter,
    ReversePrinter,
)
from app.services.serializer import JsonSerializer, XmlSerializer

DISPLAY_STRATEGIES = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay,
}

PRINT_STRATEGIES = {
    "console": ConsolePrinter,
    "reverse": ReversePrinter,
}

SERIALIZER_STRATEGIES = {
    "json": JsonSerializer,
    "xml": XmlSerializer,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            strategy = DISPLAY_STRATEGIES[method_type]()
            strategy.display(book)
        elif cmd == "print":
            strategy = PRINT_STRATEGIES[method_type]()
            strategy.print_book(book)
        elif cmd == "serialize":
            strategy = SERIALIZER_STRATEGIES[method_type]()
            return strategy.serialize(book)

    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(
        sample_book,
        [("display", "reverse"), ("serialize", "xml")]
    ))
