from typing import Type

from app.book import Book
from app.displays import DisplayMethod, ConsoleDisplay, ReverseDisplay
from app.printers import PrintBookMethod, ConsolePrint, ReversePrint
from app.serializers import Serializer, JsonSerializer, XmlSerializer

DISPLAY_METHODS: dict[str, Type[DisplayMethod]] = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay,
}

PRINT_METHODS: dict[str, Type[PrintBookMethod]] = {
    "console": ConsolePrint,
    "reverse": ReversePrint,
}

SERIALIZERS: dict[str, Type[Serializer]] = {
    "json": JsonSerializer,
    "xml": XmlSerializer
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DISPLAY_METHODS[method_type]().display(book)
        elif cmd == "print":
            PRINT_METHODS[method_type]().print_book(book)
        elif cmd == "serialize":
            return SERIALIZERS[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
