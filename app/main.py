from typing import Type

from app.book import Book
from app.displays import Display, ConsoleDisplay, ReverseDisplay
from app.printers import Printer, ConsolePrinter, ReversePrinter
from app.serializers import Serializer, JSONserializer, XMLserializer


DISPLAY_TYPE: dict[str, Type[Display]] = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay
}

PRINTER_TYPE: dict[str, Type[Printer]] = {
    "console": ConsolePrinter,
    "reverse": ReversePrinter,
}

SERIALIZER_TYPE: dict[str, Type[Serializer]] = {
    "json": JSONserializer,
    "xml": XMLserializer
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DISPLAY_TYPE[method_type]().display(book.content)

        elif cmd == "print":
            PRINTER_TYPE[method_type]().printer(book)

        elif cmd == "serialize":
            return SERIALIZER_TYPE[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
