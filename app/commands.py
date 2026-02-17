from typing import Dict, Tuple, Optional
from .entities import Book
from .display import DisplayStrategy
from .printer import PrintStrategy
from .serializer import Serializer

Command = Tuple[str, str]  # (cmd, method_type)


class CommandProcessor:
    def __init__(
        self,
        displays: Dict[str, DisplayStrategy],
        printers: Dict[str, PrintStrategy],
        serializers: Dict[str, Serializer],
    ) -> None:
        self._displays = displays
        self._printers = printers
        self._serializers = serializers

    def run(self, book: Book, commands: list[Command]) -> Optional[str]:
        for cmd, method_type in commands:
            if cmd == "display":
                self._display(book, method_type)
            elif cmd == "print":
                self._print(book, method_type)
            elif cmd == "serialize":
                return self._serialize(book, method_type)
        return None

    def _display(self, book: Book, method_type: str) -> None:
        strategy = self._displays.get(method_type)
        if not strategy:
            # Preserve original error text
            raise ValueError(f"Unknown display type: {method_type}")
        strategy.display(book)

    def _print(self, book: Book, method_type: str) -> None:
        strategy = self._printers.get(method_type)
        if not strategy:
            raise ValueError(f"Unknown print type: {method_type}")
        strategy.print_book(book)

    def _serialize(self, book: Book, method_type: str) -> str:
        strategy = self._serializers.get(method_type)
        if not strategy:
            raise ValueError(f"Unknown serialize type: {method_type}")
        return strategy.serialize(book)
