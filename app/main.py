from __future__ import annotations

from app.book import Book
from app.display import DisplayConsole, DisplayReverse
from app.print_book import PrintConsole, PrintReverse
from app.serializer import SerializeJson, SerializeXml


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    command_mapping = {
        ("display", "console"): DisplayConsole(book).display,
        ("display", "reverse"): DisplayReverse(book).display,
        ("print", "console"): PrintConsole(book).print_book,
        ("print", "reverse"): PrintReverse(book).print_book,
        ("serialize", "json"): SerializeJson(book).serialize,
        ("serialize", "xml"): SerializeXml(book).serialize,
    }

    for cmd, method_type in commands:
        if (cmd, method_type) in command_mapping:
            return command_mapping[(cmd, method_type)]()
        else:
            raise ValueError(f"Unknown cmd {cmd} or method_type {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
