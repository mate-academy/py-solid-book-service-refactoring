from __future__ import annotations

from app.dispatchers.display_dispatcher import DisplayDispatcher
from app.dispatchers.print_dispatcher import PrintDispatcher
from app.dispatchers.serialize_dispatcher import SerializeDispatcher
from app.entities.book import Book


class CommandDispatcher:
    RETURN_COMMANDS = ["serialize"]

    ALLOWED_DISPATCHER = {
        "display": DisplayDispatcher(),
        "print": PrintDispatcher(),
        "serialize": SerializeDispatcher()
    }

    @classmethod
    def handle_output(
            cls,
            cmd: str,
            method_type: str,
            book: Book
    ) -> str | None:
        return cls.ALLOWED_DISPATCHER[cmd].handle(
            method_type=method_type,
            book=book
        )

    @classmethod
    def is_command_valid(cls, cmd: str) -> bool:
        return cmd in cls.ALLOWED_DISPATCHER
