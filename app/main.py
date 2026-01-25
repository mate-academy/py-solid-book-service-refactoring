from typing import Dict, Any

from app.model import Book
from app.display_interface import ConsoleDisplay, ReverseDisplay
from app.print_interface import ConsolePrinter, ReversePrinter
from app.serialize_interface import JSONSerializer, XMLSerializer


STRATEGIES: Dict[str, Dict[str, Any]] = {
    "display": {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    },
    "print": {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter(),
    },
    "serialize": {
        "json": JSONSerializer(),
        "xml": XMLSerializer(),
    }
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    last_result = None

    for cmd, method_type in commands:
        category = STRATEGIES.get(cmd)
        if not category:
            raise ValueError(f"Unknown command: {cmd}")

        strategy = category.get(method_type)
        if not strategy:
            raise ValueError(f"Unknown {cmd} type: {method_type}")

        result = strategy.execute(book)
        if result is not None:
            last_result = result

    return last_result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")

    output = main(sample_book, [
        ("display", "reverse"),
        ("serialize", "xml")
    ])

    print("\nSerialization Output:")
    print(output)
