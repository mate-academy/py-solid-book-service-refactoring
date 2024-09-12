from typing import Type
from app.book import Book
from app.displays import Display, ConsoleDisplay, ReverseDisplay
from app.printers import Printer, ConsolePrinter, ReversePrinter
from app.serializers import Serializer, JsonSerializer, XmlSerializer

DISPLAYS: dict[str, Type[Display]] = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay,
}
PRINTERS: dict[str, Type[Printer]] = {
    "console": ConsolePrinter,
    "reverse": ReversePrinter,
}
SERIALIZERS: dict[str, Type[Serializer]] = {
    "json": JsonSerializer,
    "xml": XmlSerializer,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DISPLAYS[method_type]().display(book.content)
        elif cmd == "print":
            PRINTERS[method_type]().print_book(book)
        elif cmd == "serialize":
            return SERIALIZERS[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
