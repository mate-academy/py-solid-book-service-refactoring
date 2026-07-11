from app.book import Book
from app.display import ConsoleDisplay, DisplayStrategy, ReverseDisplay
from app.print_book import ConsolePrintBook, PrintStrategy, ReversePrintBook
from app.serializers import JsonSerializer, SerializeStrategy, XmlSerializer

DISPLAY_STRATEGIES: dict[str, DisplayStrategy] = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}

PRINT_STRATEGIES: dict[str, PrintStrategy] = {
    "console": ConsolePrintBook(),
    "reverse": ReversePrintBook(),
}

SERIALIZE_STRATEGIES: dict[str, SerializeStrategy] = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            strategy = DISPLAY_STRATEGIES.get(method_type)
            if strategy is None:
                raise ValueError(f"Unknown display type: {method_type}")
            strategy.display(book)
        elif cmd == "print":
            strategy = PRINT_STRATEGIES.get(method_type)
            if strategy is None:
                raise ValueError(f"Unknown print type: {method_type}")
            strategy.print_book(book)
        elif cmd == "serialize":
            strategy = SERIALIZE_STRATEGIES.get(method_type)
            if strategy is None:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return strategy.serialize(book)
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
