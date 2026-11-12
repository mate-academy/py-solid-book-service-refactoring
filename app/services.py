"""Application service responsible for dispatching book commands."""

from collections.abc import Callable

from app.displayers import BookDisplayer
from app.models import Book
from app.printers import BookPrinter
from app.serializers import BookSerializer


__all__ = ["BookService"]


CommandHandler = Callable[[str], str | None]


class BookService:
    """Execute book commands using injected tools."""

    def __init__(
        self,
        book: Book,
        displayers: dict[str, BookDisplayer],
        printers: dict[str, BookPrinter],
        serializers: dict[str, BookSerializer],
    ) -> None:
        self._book = book
        self._displayers = displayers
        self._printers = printers
        self._serializers = serializers
        self._command_handlers: dict[str, CommandHandler] = {
            "display": self._display,
            "print": self._print,
            "serialize": self._serialize,
        }

    def execute(self, commands: list[tuple[str, str]]) -> str | None:
        for command, method_type in commands:
            handler = self._command_handlers.get(command)
            if handler is None:
                continue

            result = handler(method_type)
            if result is not None:
                return result
        return None

    def _display(self, display_type: str) -> None:
        try:
            displayer = self._displayers[display_type]
        except KeyError:
            raise ValueError(
                f"Unknown display type: {display_type}"
            ) from None
        displayer.display(self._book)

    def _print(self, print_type: str) -> None:
        try:
            printer = self._printers[print_type]
        except KeyError:
            raise ValueError(f"Unknown print type: {print_type}") from None
        printer.print_book(self._book)

    def _serialize(self, serialize_type: str) -> str:
        try:
            serializer = self._serializers[serialize_type]
        except KeyError:
            raise ValueError(
                f"Unknown serialize type: {serialize_type}"
            ) from None
        return serializer.serialize(self._book)
