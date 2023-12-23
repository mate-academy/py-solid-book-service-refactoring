from __future__ import annotations

from app.book_model import Book
from app.book_services import (
    print_console,
    print_reverse,
    display_console,
    display_reverse,
    serialize_to_json,
    serializer_to_xml
)


def serializer_handler(book: Book, serializer_type: str) -> str:
    if serializer_type == "json":
        return serialize_to_json(book)
    elif serializer_type == "xml":
        return serializer_to_xml(book)
    else:
        raise ValueError(f"Unknown serialize type: {serializer_type}")


def printer_handler(book: Book, printer_type: str) -> None:
    if printer_type == "console":
        print_console(book)
    elif printer_type == "reverse":
        print_reverse(book)
    else:
        raise ValueError(f"Unknown print type: {printer_type}")


def displayer_handler(book: Book, display_type: str) -> None:
    if display_type == "console":
        display_console(book)
    elif display_type == "reverse":
        display_reverse(book)
    else:
        raise ValueError(f"Unknown display type: {display_type}")


def command_handler(book: Book, command: str, method_type: str) -> None | str:
    if command == "display":
        displayer_handler(book, method_type)
    elif command == "print":
        printer_handler(book, method_type)
    elif command == "serialize":
        return serializer_handler(book, method_type)
    else:
        raise ValueError(f"Unknown command type: {command}")
