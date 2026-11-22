from typing import Callable

from app.book import Book
from app.displays import get_display
from app.printers import get_printer
from app.serializers import get_serializer


def display_command(book: Book, method_type: str) -> None:
    get_display(method_type).display(book)


def print_command(book: Book, method_type: str) -> None:
    get_printer(method_type).print_book(book)


def serialize_command(book: Book, method_type: str) -> str:
    return get_serializer(method_type).serialize(book)


COMMANDS: dict[str, Callable[[Book, str], None | str]] = {
    "display": display_command,
    "print": print_command,
    "serialize": serialize_command,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        handler = COMMANDS.get(cmd)
        if handler is None:
            continue
        result = handler(book, method_type)
        if result is not None:
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
