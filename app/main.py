from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.serializer import JsonSerializer, XmlSerializer

DISPLAY_METHODS = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}

PRINT_METHODS = {
    "console": ConsolePrinter(),
    "reverse": ReversePrinter(),
}

SERIALIZE_METHODS = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type not in DISPLAY_METHODS:
                raise ValueError(f"Unknown display type: {method_type}")
            DISPLAY_METHODS[method_type].display(book)

        elif cmd == "print":
            if method_type not in PRINT_METHODS:
                raise ValueError(f"Unknown print type: {method_type}")
            PRINT_METHODS[method_type].print_book(book)

        elif cmd == "serialize":
            if method_type not in SERIALIZE_METHODS:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return SERIALIZE_METHODS[method_type].serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
