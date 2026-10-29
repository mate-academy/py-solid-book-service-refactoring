from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print_book import ConsolePrinter, ReversePrinter
from app.serialize import JsonBookSerializer, XmlBookSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displays = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }

    printers = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter(),
    }

    serializers = {
        "json": JsonBookSerializer(),
        "xml": XmlBookSerializer(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            if method_type not in displays:
                raise ValueError(f"Unknown display type: {method_type}")

            displays[method_type].display(book)

        elif cmd == "print":
            if method_type not in printers:
                raise ValueError(f"Unknown print type: {method_type}")

            printers[method_type].print_book(book)

        elif cmd == "serialize":
            if method_type not in serializers:
                raise ValueError(f"Unknown serialize type: {method_type}")

            return serializers[method_type].serialize(book)


if __name__ == "__main__":
    sample_book = Book(
        "Sample Book",
        "This is some sample content.",
    )

    print(main(
        sample_book,
        [
            ("display", "reverse"),
            ("serialize", "xml"),
        ],
    ))
