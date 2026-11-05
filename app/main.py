from app.models import Book
from app.service import (
    ConsoleDisplay,
    ConsolePrint,
    JSONSerializer,
    XMLSerializer,
    ReversePrint,
    ReverseDisplay,
    DisplayStrategy,
    PrintStrategy,
    SerializeStrategy
)


DISPLAY_STRATEGIES: dict[str, DisplayStrategy] = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}

PRINT_STRATEGIES: dict[str, PrintStrategy] = {
    "console": ConsolePrint(),
    "reverse": ReversePrint(),
}

SERIALIZE_STRATEGIES: dict[str, SerializeStrategy] = {
    "json": JSONSerializer(),
    "xml": XMLSerializer(),
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    last_result = None

    for cmd, method_type in commands:
        if cmd == "display":
            strategy = DISPLAY_STRATEGIES.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown display type: {method_type}")
            strategy.display(book)

        elif cmd == "print":
            strategy = PRINT_STRATEGIES.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown print type: {method_type}")
            strategy.print_book(book)

        elif cmd == "serialize":
            strategy = SERIALIZE_STRATEGIES.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown serialize type: {method_type}")
            last_result = strategy.serialize(book)

    return last_result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
