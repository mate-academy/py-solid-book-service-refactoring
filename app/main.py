from app.book import (
    Book,
    DisplayBook,
    PrintBook,
    BookSerializer,
    ConsoleDisplay,
    ReverseDisplay,
    ConsolePrint,
    ReversePrint,
    JSONBookSerializer,
    XMLBookSerializer,
)


def main(
    book: Book,
    commands: list[tuple[str, str]],
    displays: dict[str, DisplayBook] | None = None,
    prints: dict[str, PrintBook] | None = None,
    serializers: dict[str, BookSerializer] | None = None,
) -> None | str:

    if displays is None:
        displays = {
            "console": ConsoleDisplay(),
            "reverse": ReverseDisplay(),
        }

    if prints is None:
        prints = {
            "console": ConsolePrint(),
            "reverse": ReversePrint(),
        }

    if serializers is None:
        serializers = {
            "json": JSONBookSerializer(),
            "xml": XMLBookSerializer(),
        }

    for cmd, method_type in commands:
        if cmd == "display":
            if method_type not in displays:
                raise ValueError(f"Unknown display type: {method_type}")
            displays[method_type].display(book)

        elif cmd == "print":
            if method_type not in prints:
                raise ValueError(f"Unknown print type: {method_type}")
            prints[method_type].print_book(book)

        elif cmd == "serialize":
            if method_type not in serializers:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serializers[method_type].serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")

    displays = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }

    prints = {
        "console": ConsolePrint(),
        "reverse": ReversePrint(),
    }

    serializers = {
        "json": JSONBookSerializer(),
        "xml": XMLBookSerializer(),
    }

    print(main(
        sample_book,
        [("display", "reverse"), ("serialize", "xml")],
        displays,
        prints,
        serializers,
    ))
