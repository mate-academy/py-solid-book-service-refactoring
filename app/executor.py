from __future__ import annotations
from dataclasses import dataclass
from typing import Callable, Optional

from .book import Book
from .display import get_display_strategy
from .printing import get_print_strategy
from .serialization import get_serializer


@dataclass(frozen=True)
class Command:
    cmd: str
    method_type: str


Handler = Callable[[Book, Command], Optional[str]]


class BookCommandExecutor:
    def __init__(self) -> None:
        self._handlers: dict[str, Handler] = {
            "display": self._handle_display,
            "print": self._handle_print,
            "serialize": self._handle_serialize,
        }

    def execute(self, book: Book, commands: list[Command]) -> Optional[str]:
        serialized_result: Optional[str] = None

        for command in commands:
            handler = self._handlers.get(command.cmd)
            if handler is None:
                raise ValueError(f"Unknown command: {command.cmd}")

            result = handler(book, command)

            if command.cmd == "serialize":
                serialized_result = result

        return serialized_result

    @staticmethod
    def _handle_display(book: Book, command: Command) -> None:
        strategy = get_display_strategy(command.method_type)
        strategy.display(book)
        return None

    @staticmethod
    def _handle_print(book: Book, command: Command) -> None:
        strategy = get_print_strategy(command.method_type)
        strategy.print_book(book)
        return None

    @staticmethod
    def _handle_serialize(book: Book, command: Command) -> str:
        serializer = get_serializer(command.method_type)
        return serializer.serialize(book)
