from typing import Any

from app.display import ConsoleDisplay, ReverseDisplay
from app.models import Book
from app.printer import ConsolePrinter, ReversePrinter
from app.serializers import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> Any:
    displays = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }
    printers = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter(),
    }
    serializers = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }

    result = None
    for action, method in commands:
        if action == "display":
            displays[method].display(book)
        elif action == "print":
            printers[method].print_book(book)
        elif action == "serialize":
            result = serializers[method].serialize(book)

    return result
