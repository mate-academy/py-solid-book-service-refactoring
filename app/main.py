from __future__ import annotations

from app.display import BookDisplayer
from app.printer import BookPrinter
from app.serializer import BookSerializer


class Book:
    """Entity that stores book data only."""

    def __init__(
        self,
        title: str,
        content: str,
        displayer: BookDisplayer,
        printer: BookPrinter,
        serializer: BookSerializer,
    ):
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


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            book.print_book(method_type)
        elif cmd == "serialize":
            return book.serialize(method_type)
    return None


if __name__ == "__main__":
    displayer = BookDisplayer()
    printer = BookPrinter()
    serializer = BookSerializer()

    sample = Book("Sample", "Content", displayer, printer, serializer)
    print(main(sample, [("display", "reverse"), ("serialize", "xml")]))
