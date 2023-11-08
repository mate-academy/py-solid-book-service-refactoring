from __future__ import annotations

from app.book import Book
from app.display import DisplayConsole, DisplayReverse
from app.print_book import PrintConsole, PrintReverse
from app.serialize import SerializerXML, SerializerJSON


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_methods = {
        "console": DisplayConsole.display,
        "reverse": DisplayReverse.display,
    }

    print_methods = {
        "console": PrintConsole.print_book,
        "reverse": PrintReverse.print_book,
    }

    serialize_methods = {
        "json": SerializerJSON.serialize,
        "xml": SerializerXML.serialize,
    }

    command_mappings = {
        "display": display_methods,
        "print": print_methods,
        "serialize": serialize_methods,
    }

    for cmd, method_type in commands:
        method_mapping = command_mappings.get(cmd)
        if method_mapping:
            method = method_mapping.get(method_type)
            if method:
                return method(book)
            else:
                raise ValueError(f"Unknown {cmd} type: {method_type}")
        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
