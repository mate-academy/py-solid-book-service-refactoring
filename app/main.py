from typing import Type

from app.book import Book
from app.printers import Printer, ConsolePrinter, ReversePrinter
from app.serializers import Serializer, JSONSerializer, XMLSerializer
from app.displays import Display, ConsoleDisplay, ReverseDisplay


DISPLAY_STRATEGIES: dict[str, Type[Display]] = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay,
}

PRINT_STRATEGIES: dict[str, Type[Printer]] = {
    "console": ConsolePrinter,
    "reverse": ReversePrinter,
}

SERIALIZER_STRATEGIES: dict[str, Type[Serializer]] = {
    "json": JSONSerializer,
    "xml": XMLSerializer,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DISPLAY_STRATEGIES[method_type]().display(book.content)

        elif cmd == "print":
            PRINT_STRATEGIES[method_type]().print_book(book)

        elif cmd == "serialize":
            SERIALIZER_STRATEGIES[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
