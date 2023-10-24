from __future__ import annotations

from app.books import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print import ConsolePrint, ReversePrint
from app.serializers import JsonSerializer, XmlSerializer


DISPLAY = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay
}

PRINT = {
    "console": ConsolePrint,
    "reverse": ReversePrint
}

SERIALIZERS = {
    "json": JsonSerializer,
    "xml": XmlSerializer
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DISPLAY[method_type]().display(book)
        elif cmd == "print":
            PRINT[method_type]().print_book(book)
        elif cmd == "serialize":
            return SERIALIZERS[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
