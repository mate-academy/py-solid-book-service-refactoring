from __future__ import annotations

from typing import Optional

from app.models import Book
from app.displays import ConsoleDisplay, Display, ReverseDisplay
from app.printers import ConsolePrinter, Printer, ReversePrinter
from app.serializers import JsonSerializer, Serializer, XmlSerializer


DEFAULT_DISPLAYS: dict[str, Display] = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}

DEFAULT_PRINTERS: dict[str, Printer] = {
    "console": ConsolePrinter(),
    "reverse": ReversePrinter(),
}

DEFAULT_SERIALIZERS: dict[str, Serializer] = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}


def main(
    book: Book,
    commands: list[tuple[str, str]],
    *,
    displays: dict[str, Display] = DEFAULT_DISPLAYS,
    printers: dict[str, Printer] = DEFAULT_PRINTERS,
    serializers: dict[str, Serializer] = DEFAULT_SERIALIZERS,
) -> Optional[str]:

    for cmd, method in commands:
        if cmd == "display":
            displays[method].show(book)
        elif cmd == "print":
            printers[method].print(book)
        elif cmd == "serialize":
            return serializers[method].serialize(book)
        else:
            raise ValueError(f"Unknown command: {cmd}")

    return None


if __name__ == "__main__":
    sample_book = Book(
        title="Sample Book",
        content="This is some sample content."
    )

    displays = DEFAULT_DISPLAYS
    printers = DEFAULT_PRINTERS
    serializers = DEFAULT_SERIALIZERS

    result = main(
        sample_book,
        [("display", "reverse"), ("serialize", "xml")],
        displays=displays,
        printers=printers,
        serializers=serializers,
    )
    if result is not None:
        print(result)
