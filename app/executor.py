from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from .book import Book
from .display import get_display_strategy
from app.printing import get_print_strategy
from app.serialization import get_serializer


@dataclass(frozen=True)
class Command:
    cmd: str
    method_type: str


class BookCommandExecutor:
    def execute(self, book: Book, commands: list[Command]) -> Optional[str]:
        for command in commands:
            if command.cmd == "display":
                strategy = get_display_strategy(command.method_type)
                strategy.display(book)

            elif command.cmd == "print":
                strategy = get_print_strategy(command.method_type)
                strategy.print_book(book)

            elif command.cmd == "serialize":
                serializer = get_serializer(command.method_type)
                return serializer.serialize(book)

        return None
