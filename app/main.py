from app.book import Book

from app.display import ConsoleDisplay, ReverseDisplay
from app.printing import ConsolePrint, ReversePrint
from app.serializer import JsonSerializer, XmlSerializer


DISPLAY_TYPES = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}

PRINT_TYPES = {
    "console": ConsolePrint(),
    "reverse": ReversePrint(),
}

SERIALIZE_TYPES = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            try:
                DISPLAY_TYPES[method_type].display(book)
            except KeyError:
                raise ValueError(f"Unknown display type: {method_type}")

        elif cmd == "print":
            try:
                PRINT_TYPES[method_type].print_book(book)
            except KeyError:
                raise ValueError(f"Unknown print type: {method_type}")

        elif cmd == "serialize":
            try:
                return SERIALIZE_TYPES[method_type].serialize(book)
            except KeyError:
                raise ValueError(f"Unknown serialize type: {method_type}")

    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
