from app.book import Book
from app.display_strategy import (
    DisplayStrategy,
    ConsoleDisplayStrategy,
    ReverseDisplayStrategy
)
from app.print_strategy import (
    PrintStrategy,
    ConsolePrintStrategy,
    ReversePrintStrategy
)
from app.serialize_strategy import (
    SerializeStrategy,
    JsonSerializeStrategy,
    XmlSerializeStrategy
)


def get_display_strategy(method_type: str) -> DisplayStrategy:
    if method_type == "console":
        return ConsoleDisplayStrategy()
    elif method_type == "reverse":
        return ReverseDisplayStrategy()
    else:
        raise ValueError(f"Unknown display type: {method_type}")


def get_print_strategy(method_type: str) -> PrintStrategy:
    if method_type == "console":
        return ConsolePrintStrategy()
    elif method_type == "reverse":
        return ReversePrintStrategy()
    else:
        raise ValueError(f"Unknown print type: {method_type}")


def get_serialize_strategy(method_type: str) -> SerializeStrategy:
    if method_type == "json":
        return JsonSerializeStrategy()
    elif method_type == "xml":
        return XmlSerializeStrategy()
    else:
        raise ValueError(f"Unknown serialize type: {method_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            strategy = get_display_strategy(method_type)
            return strategy.display(book.title, book.content)
        elif cmd == "print":
            strategy = get_print_strategy(method_type)
            return strategy.print(book.title, book.content)
        elif cmd == "serialize":
            strategy = get_serialize_strategy(method_type)
            return strategy.serialize(book.title, book.content)
        return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
