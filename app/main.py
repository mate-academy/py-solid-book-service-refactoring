from __future__ import annotations

from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print_book import ConsolePrint, ReversePrint
from app.serialize import JsonSerialize, XmlSerialize

DISPLAY_MAP = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}

PRINT_MAP = {
    "console": ConsolePrint(),
    "reverse": ReversePrint(),
}

SERIALIZE_MAP = {
    "json": JsonSerialize(),
    "xml": XmlSerialize(),
}


def main(
    book: Book, commands: list[tuple[str, str]]
) -> str | None:
    for cmd, method_type in commands:
        if cmd == "display":
            handler = DISPLAY_MAP.get(method_type)
            if handler is None:
                raise ValueError(
                    f"Unknown display type: {method_type}"
                )
            handler.display(book)
        elif cmd == "print":
            handler = PRINT_MAP.get(method_type)
            if handler is None:
                raise ValueError(
                    f"Unknown print type: {method_type}"
                )
            handler.print_book(book)
        elif cmd == "serialize":
            handler = SERIALIZE_MAP.get(method_type)
            if handler is None:
                raise ValueError(
                    f"Unknown serialize type: {method_type}"
                )
            return handler.serialize(book)
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(
        main(
            sample_book,
            [("display", "reverse"), ("serialize", "xml")],
        )
    )
