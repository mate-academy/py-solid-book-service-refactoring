from __future__ import annotations

from app.book import Book
from app.display import DisplayConsole, DisplayReverse
from app.print_book import PrintConsole, PrintReverse
from app.serializer import SerializeJson, SerializeXml


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                DisplayConsole.display(book)
            elif method_type == "reverse":
                DisplayReverse.display(book)
        elif cmd == "print":
            if method_type == "console":
                PrintConsole.print_book(book)
            elif method_type == "reverse":
                PrintReverse.print_book(book)
        elif cmd == "serialize":
            if method_type == "json":
                return SerializeJson.serialize(book)
            elif method_type == "xml":
                return SerializeXml.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
