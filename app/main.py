from __future__ import annotations

from typing import Optional

from app.display import BookDisplayer
from app.printer import BookPrinter
from app.serializer import BookSerializer


class Book:
    """Book entity that stores data and delegates actions to injected services."""

    def __init__(
        self,
        title: str,
        content: str,
        displayer: BookDisplayer,
        printer: BookPrinter,
        serializer: BookSerializer,
    ) -> None:
        self.title = title
        self.content = content
        self._displayer = displayer
        self._printer = printer
        self._serializer = serializer

    def display(self, display_type: str) -> None:
        self._displayer.display(self, display_type)

    def print_book(self, print_type: str) -> None:
        self._printer.print_book(self, print_type)

    def serialize(self, serialize_type: str) -> str:
        return self._serializer.serialize(self, serialize_type)


def main(book: Book, commands: list[tuple[str, str]]) -> Optional[str]:
    for command, method_type in commands:
        if command == "display":
            book.display(method_type)
            continue

        if command == "print":
            book.print_book(method_type)
            continue

        if command == "serialize":
            return book.serialize(method_type)

    return None


def run_example() -> None:
    displayer = BookDisplayer()
    printer = BookPrinter()
    serializer = BookSerializer()

    sample_book = Book(
        title="Sample",
        content="Content",
        displayer=displayer,
        printer=printer,
        serializer=serializer,
    )

    result = main(sample_book, [("display", "reverse"),
                                ("serialize", "xml")])
    print(result)


if __name__ == "__main__":
    run_example()
