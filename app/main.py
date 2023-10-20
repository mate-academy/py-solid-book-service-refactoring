from __future__ import annotations

from app.book import Book
from app.displays import ConsoleDisplay, ReverseDisplay
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import JsonSerializer, XmlSerializer


DISPLAYS = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay
}

PRINTERS = {
    "console": ConsolePrinter,
    "reverse": ReversePrinter
}

SERIALIZERS = {
    "json": JsonSerializer,
    "xml": XmlSerializer
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DISPLAYS[method_type]().display(book)
        elif cmd == "print":
            PRINTERS[method_type]().print_book(book)
        elif cmd == "serialize":
            return SERIALIZERS[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
