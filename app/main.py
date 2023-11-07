from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.serializers import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    commands_dict = {
        "display": {
            "console": ConsoleDisplay.display,
            "reverse": ReverseDisplay.display,
        },
        "print": {
            "console": ConsolePrinter.printer,
            "reverse": ReversePrinter.printer,
        },
        "serialize": {
            "json": JsonSerializer.serialize,
            "xml": XmlSerializer.serialize,
        },
    }

    for cmd, method_type in commands:
        if cmd == "display":
            if method_type not in ("console", "reverse"):
                raise ValueError(f"Unknown display type: {method_type}")
            commands_dict[cmd][method_type](book)
        elif cmd == "print":
            if method_type not in ("console", "reverse"):
                raise ValueError(f"Unknown print type: {method_type}")
            commands_dict[cmd][method_type](book)
        elif cmd == "serialize":
            if method_type not in ("json", "xml"):
                raise ValueError(f"Unknown serialize type: {method_type}")
            return commands_dict[cmd][method_type](book)


if __name__ == "__main__":
    sample_book = Book(
        title="Sample Book",
        content="This is some sample content."
    )
    print(main(sample_book, [("display", "console"), ("serialize", "xml")]))
