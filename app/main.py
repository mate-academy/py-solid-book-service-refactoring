from .models import Book
from .strategies import (
    DISPLAY_STRATEGIES,
    PRINTER_STRATEGIES,
    SERIALIZER_STRATEGIES
)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    result = None

    for cmd, method_type in commands:
        if cmd == "display":
            if strategy := DISPLAY_STRATEGIES.get(method_type):
                strategy.display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")

        elif cmd == "print":
            if strategy := PRINTER_STRATEGIES.get(method_type):
                strategy.print_book(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")

        elif cmd == "serialize":
            if strategy := SERIALIZER_STRATEGIES.get(method_type):
                result = strategy.serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
