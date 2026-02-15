from __future__ import annotations

from app.models import Book
from app.services import (
    ConsoleDisplay,
    ReverseDisplay,
    ConsolePrint,
    ReversePrint,
    JsonSerializer,
    XmlSerializer,
)
from app.validators import BookValidator


def main(book: Book, actions: list[tuple[str, str]]) -> str | None:
    BookValidator.validate(book)

    for action, action_type in actions:

        if action == "display":
            if action_type == "console":
                strategy = ConsoleDisplay()
            elif action_type == "reverse":
                strategy = ReverseDisplay()
            else:
                raise ValueError(f"Unknown display type: {action_type}")

            strategy.display(book)

        elif action == "print":
            if action_type == "console":
                printer = ConsolePrint()
            elif action_type == "reverse":
                printer = ReversePrint()
            else:
                raise ValueError(f"Unknown print type: {action_type}")

            printer.print_book(book)

        elif action == "serialize":
            if action_type == "json":
                serializer = JsonSerializer()
            elif action_type == "xml":
                serializer = XmlSerializer()
            else:
                raise ValueError(f"Unknown serializer type: {action_type}")

            return serializer.serialize(book)

    return None
