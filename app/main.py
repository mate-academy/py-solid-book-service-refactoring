from app.models import Book
from app.services import (ConsolePrinter, ReversePrinter,
                          DisplayConsole, DisplayReverse)
from app.serializers import JsonSerialize, XmlSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    display_strategies = {"console": DisplayConsole(),
                          "reverse": DisplayReverse()}
    print_strategies = {"console": ConsolePrinter(),
                        "reverse": ReversePrinter()}
    serialize_strategies = {"json": JsonSerialize(),
                            "xml": XmlSerialize()}

    result = None

    for cmd, method_type in commands:
        if cmd == "display":
            strategy = display_strategies.get(method_type)
            if strategy:
                strategy.display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")

        elif cmd == "print":
            strategy = print_strategies.get(method_type)
            if strategy:
                strategy.print_book(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")

        elif cmd == "serialize":
            strategy = serialize_strategies.get(method_type)
            if strategy:
                result = strategy.serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
        else:
            raise ValueError(f"Unknown command: {cmd}")

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
