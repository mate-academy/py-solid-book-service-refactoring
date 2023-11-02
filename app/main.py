from __future__ import annotations

import json
import xml.etree.ElementTree as ET

from app.book import Book
from app.display import DisplayConsole, DisplayReverse
from app.print_book import PrintConsole, PrintReverse
from app.serialize import SerializerXML, SerializerJSON


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                DisplayConsole.display(book)
            elif method_type == "reverse":
                DisplayReverse.display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")

        elif cmd == "print":
            if method_type == "console":
                PrintConsole.print_book(book)
            elif method_type == "reverse":
                PrintReverse.print_book(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")

        elif cmd == "serialize":
            if method_type == "json":
                return SerializerJSON.serialize(book)
            elif method_type == "xml":
                return SerializerXML.serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {serialize_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
