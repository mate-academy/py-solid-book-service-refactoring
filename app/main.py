from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrint, ReversePrint
from app.serializer import JsonSerializer, XmlSerializer

DISPLAY_STRATEGIES = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}

PRINT_STRATEGIES = {
    "console": ConsolePrint(),
    "reverse": ReversePrint(),
}

SERIALIZER_STRATEGIES = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type not in DISPLAY_STRATEGIES:
                raise ValueError(f"Unknown display type: {method_type}")
            DISPLAY_STRATEGIES[method_type].display(book)

        elif cmd == "print":
            if method_type not in PRINT_STRATEGIES:
                raise ValueError(f"Unknown print type: {method_type}")
            PRINT_STRATEGIES[method_type].print_book(book)

        elif cmd == "serialize":
            if method_type not in SERIALIZER_STRATEGIES:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return SERIALIZER_STRATEGIES[method_type].serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
