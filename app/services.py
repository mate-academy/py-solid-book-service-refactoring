from app.book import Book
from app.displays import (
    BookDisplay,
    ConsoleBookDisplay,
    ReverseBookDisplay,
)
from app.printers import (
    BookPrinter,
    ConsoleBookPrinter,
    ReverseBookPrinter,
)
from app.serializers import (
    BookSerializer,
    JsonBookSerializer,
    XmlBookSerializer,
)


class BookService:
    def __init__(self, book: Book) -> None:
        self.book = book

        self.displays: dict[str, BookDisplay] = {
            "console": ConsoleBookDisplay(),
            "reverse": ReverseBookDisplay(),
        }

        self.printers: dict[str, BookPrinter] = {
            "console": ConsoleBookPrinter(),
            "reverse": ReverseBookPrinter(),
        }

        self.serializers: dict[str, BookSerializer] = {
            "json": JsonBookSerializer(),
            "xml": XmlBookSerializer(),
        }

    def display(self, display_type: str) -> None:
        try:
            display = self.displays[display_type]
        except KeyError:
            raise ValueError(
                f"Unknown display type: {display_type}"
            ) from None

        display.display(self.book)

    def print_book(self, print_type: str) -> None:
        try:
            printer = self.printers[print_type]
        except KeyError:
            raise ValueError(
                f"Unknown print type: {print_type}"
            ) from None

        printer.print_book(self.book)

    def serialize(self, serialize_type: str) -> str:
        try:
            serializer = self.serializers[serialize_type]
        except KeyError:
            raise ValueError(
                f"Unknown serialize type: {serialize_type}"
            ) from None

        return serializer.serialize(self.book)
