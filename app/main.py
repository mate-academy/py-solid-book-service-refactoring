from __future__ import annotations
from app.models.book import Book
from app.services.printer import BookConsoleDisplayer, BookPrinter
from app.services.serializer import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displayer = BookConsoleDisplayer()
    printer = BookPrinter()

    for cmd, method_type in commands:
        if cmd == "display":
            displayer.display(book, method_type)
        elif cmd == "print":
            printer.print_book(book, method_type)
        elif cmd == "serialize":
            if method_type == "json":
                return JsonSerializer.serialize(book)
            elif method_type == "xml":
                return XmlSerializer.serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")

    return None
