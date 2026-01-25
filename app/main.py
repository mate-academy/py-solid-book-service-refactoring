from __future__ import annotations

from typing import Optional

from app.display import BookDisplayer
from app.printer import BookPrinter
from app.serializer import BookSerializer

# Default dependencies are created OUTSIDE the Book class.
# Book does not create dependencies itself (DIP friendly),
# but tests can still instantiate Book with only title/content.
DEFAULT_DISPLAYER = BookDisplayer()
DEFAULT_PRINTER = BookPrinter()
DEFAULT_SERIALIZER = BookSerializer()


class Book:
    """Entity that stores book data and
    delegates actions to injected services."""

    def __init__(
        self,
        title: str,
        content: str,
        displayer: BookDisplayer = DEFAULT_DISPLAYER,
        printer: BookPrinter = DEFAULT_PRINTER,
        serializer: BookSerializer = DEFAULT_SERIALIZER,
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
        elif command == "print":
            book.print_book(method_type)
        elif command == "serialize":
            return book.serialize(method_type)
    return None


def run_example() -> None:
    sample = Book("Sample", "Content")  # works for tests too
    print(main(sample, [("display", "reverse"), ("serialize", "xml")]))


if __name__ == "__main__":
    run_example()
