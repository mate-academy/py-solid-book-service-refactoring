from typing import Any

from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printing import ConsolePrint, ReversePrint
from app.serializer import JsonSerializer, XmlSerializer


def create_display(book: Book, method_type: str) -> Any:
    displayers = {
        "console": ConsoleDisplay,
        "reverse": ReverseDisplay,
    }
    displayer_class = displayers.get(method_type)
    if displayer_class:
        return displayer_class(book)
    else:
        raise ValueError(f"Unknown display type {method_type}")


def create_print(book: Book, method_type: str) -> Any:
    printers = {
        "console": ConsolePrint,
        "reverse": ReversePrint,
    }
    printer_class = printers.get(method_type)
    if printer_class:
        return printer_class(book)
    else:
        raise ValueError(f"Unknown print type {method_type}")


def create_serializer(book: Book, method_type: str) -> Any:
    serializers = {
        "json": JsonSerializer,
        "xml": XmlSerializer,
    }
    serializer_class = serializers.get(method_type)
    if serializer_class:
        return serializer_class(book)
    else:
        raise ValueError(f"Unknown serialize type: {method_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            displayer = create_display(book, method_type)
            displayer.display_book()

        elif cmd == "print":
            printer = create_print(book, method_type)
            printer.print_book()

        elif cmd == "serialize":
            serializer = create_serializer(book, method_type)
            return serializer.serialize_book()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
