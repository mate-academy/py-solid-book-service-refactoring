from typing import List, Tuple

from .models import Book
from .display import ConsoleDisplay, ReverseDisplay
from .printers import ConsolePrinter, ReversePrinter
from .serializers import JsonSerializer, XmlSerializer
from .commands import (
    execute_display,
    execute_print,
    execute_serialize,
)


def main(book: Book, commands: List[Tuple[str, str]]) -> str | None:
    for command, method in commands:
        if command == "display":
            display_strategy = _get_display_strategy(method)
            execute_display(book, display_strategy)

        elif command == "print":
            printer = _get_printer(method)
            execute_print(book, printer)

        elif command == "serialize":
            serializer = _get_serializer(method)
            return execute_serialize(book, serializer)

        else:
            raise ValueError(f"Unknown command: {command}")


def _get_display_strategy(method: str) -> ConsoleDisplay | ReverseDisplay:
    if method == "console":
        return ConsoleDisplay()
    if method == "reverse":
        return ReverseDisplay()
    raise ValueError(f"Unknown display method: {method}")


def _get_printer(method: str) -> ConsolePrinter | ReversePrinter:
    if method == "console":
        return ConsolePrinter()
    if method == "reverse":
        return ReversePrinter()
    raise ValueError(f"Unknown print method: {method}")


def _get_serializer(method: str) -> JsonSerializer | XmlSerializer:
    if method == "json":
        return JsonSerializer()
    if method == "xml":
        return XmlSerializer()
    raise ValueError(f"Unknown serialize method: {method}")
