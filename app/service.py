from collections.abc import Mapping

from app.book import Book
from app.display import BookDisplay
from app.printer import BookPrinter
from app.serializer import BookSerializer


class BookService:
    def __init__(
        self,
        displays: Mapping[str, BookDisplay],
        printers: Mapping[str, BookPrinter],
        serializers: Mapping[str, BookSerializer]
    ) -> None:
        self.displays = dict(displays)
        self.printers = dict(printers)
        self.serializers = dict(serializers)

    def display(self, book: Book, display_type: str) -> None:
        display = self.displays.get(display_type)
        if display is None:
            raise ValueError(f"Unknown display type: {display_type}")
        display.display(book)

    def print_book(self, book: Book, print_type: str) -> None:
        printer = self.printers.get(print_type)
        if printer is None:
            raise ValueError(f"Unknown print type: {print_type}")
        printer.print_book(book)

    def serialize(self, book: Book, serialize_type: str) -> str:
        serializer = self.serializers.get(serialize_type)
        if serializer is None:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
        return serializer.serialize(book)
