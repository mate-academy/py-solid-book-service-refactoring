from typing import Type

from app.books import Book
from app.display_service import Display, ConsoleDisplay, ReverseDisplay
from app.serialize_service import Serializer, JsonSerializer, XmlSerializer
from app.print_service import Printer, ConsolePrinter, ReversePrinter


DISPLAY_STRATEGIES: dict[str, Type[Display]] = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay,
}

PRINT_STRATEGIES: dict[str, Type[Printer]] = {
    "console": ConsolePrinter,
    "reverse": ReversePrinter,
}

SERIALIZER_STRATEGIES: dict[str, Type[Serializer]] = {
    "json": JsonSerializer,
    "xml": XmlSerializer,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DISPLAY_STRATEGIES[method_type]().display(book.content)

        elif cmd == "print":
            PRINT_STRATEGIES[method_type]().print_book(book)

        elif cmd == "serialize":
            return SERIALIZER_STRATEGIES[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
