from typing import Protocol

from app.displays import DISPLAYERS, BookDisplay
from app.models import Book
from app.printers import PRINTERS, BookPrinter
from app.serializers import SERIALIZERS, BookSerializer

BookCommand = tuple[str, str]


class BookCommandHandler(Protocol):
    def handle(self, book: Book, method_type: str) -> None | str:
        pass


class DisplayCommandHandler:
    def __init__(self, displayers: dict[str, BookDisplay]) -> None:
        self._displayers = displayers

    def handle(self, book: Book, method_type: str) -> None:
        display_type = method_type
        if display_type not in self._displayers:
            raise ValueError(f"Unknown display type: {display_type}")

        self._displayers[display_type].display(book)


class PrintCommandHandler:
    def __init__(self, printers: dict[str, BookPrinter]) -> None:
        self._printers = printers

    def handle(self, book: Book, method_type: str) -> None:
        print_type = method_type
        if print_type not in self._printers:
            raise ValueError(f"Unknown print type: {print_type}")

        self._printers[print_type].print_book(book)


class SerializeCommandHandler:
    def __init__(self, serializers: dict[str, BookSerializer]) -> None:
        self._serializers = serializers

    def handle(self, book: Book, method_type: str) -> str:
        serialize_type = method_type
        if serialize_type not in self._serializers:
            raise ValueError(f"Unknown serialize type: {serialize_type}")

        return self._serializers[serialize_type].serialize(book)


class BookCommandProcessor:
    def __init__(
        self,
        command_handlers: dict[str, BookCommandHandler],
    ) -> None:
        self._command_handlers = command_handlers

    def execute(self, book: Book, commands: list[BookCommand]) -> None | str:
        for command_name, method_type in commands:
            if command_name not in self._command_handlers:
                continue

            result = self._command_handlers[command_name].handle(
                book, method_type
            )
            if result is not None:
                return result

        return None


def create_default_book_processor() -> BookCommandProcessor:
    return BookCommandProcessor(
        {
            "display": DisplayCommandHandler(DISPLAYERS),
            "print": PrintCommandHandler(PRINTERS),
            "serialize": SerializeCommandHandler(SERIALIZERS),
        }
    )
