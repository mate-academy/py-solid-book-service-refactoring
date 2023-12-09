from __future__ import annotations

from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrintBook, ReversePrintBook
from app.serializers import JsonSerializer, XmlSerializer


def display(book: Book, display_type: str) -> None:
    display_options = {
        "console": ConsoleDisplay,
        "reverse": ReverseDisplay,
    }

    book_to_display = display_options[display_type]

    if book_to_display:
        book_to_display(book).display_book()
    else:
        raise ValueError(f"Unknown display type: {display_type}")


def print_book(book: Book, print_type: str) -> None:
    print_options = {
        "console": ConsolePrintBook,
        "reverse": ReversePrintBook,
    }

    book_to_print = print_options[print_type]

    if book_to_print:
        book_to_print(book).print_book()
    else:
        raise ValueError(f"Unknown print type: {print_type}")


def serialize(book: Book, serialize_type: str) -> str:
    serialize_options = {
        "json": JsonSerializer,
        "xml": XmlSerializer,
    }

    book_to_serialize = serialize_options[serialize_type]

    if book_to_serialize:
        return book_to_serialize(book).serialize()
    else:
        raise ValueError(f"Unknown serialize type: {serialize_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display(book, method_type)
        elif cmd == "print":
            print_book(book, method_type)
        elif cmd == "serialize":
            return serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
