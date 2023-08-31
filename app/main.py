from __future__ import annotations

from app.entities.book import Book

from app.dispatchers.command_dispatcher import CommandDispatcher
from app.dispatchers.display_dispatcher import DisplayDispatcher
from app.dispatchers.print_dispatcher import PrintDispatcher
from app.dispatchers.serialize_dispatcher import SerializeDispatcher

from app.printers.printers import ConsolePrinter, ReversePrinter
from app.displayers.displayers import ConsoleDisplayer, ReverseDisplayer
from app.serializers.serializers import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> str:
    allowed_serializers = {
        "json": JsonSerializer(book=book),
        "xml": XmlSerializer(book=book)
    }

    allowed_printers = {
        "console": ConsolePrinter(book=book),
        "reverse": ReversePrinter(book=book)
    }

    allowed_displayers = {
        "console": ConsoleDisplayer(book=book),
        "reverse": ReverseDisplayer(book=book)
    }
    allowed_dispatcher = {
        "display": DisplayDispatcher(
            allowed_displayers=allowed_displayers
        ),
        "print": PrintDispatcher(
            allowed_printers=allowed_printers
        ),
        "serialize": SerializeDispatcher(
            allowed_serializers=allowed_serializers
        )
    }

    command_dispatcher = CommandDispatcher(
        allowed_dispatcher=allowed_dispatcher
    )

    for cmd, method_type in commands:
        if command_dispatcher.is_command_valid(cmd):
            output = command_dispatcher.handle_output(cmd, method_type)

            if cmd in command_dispatcher.RETURN_COMMANDS:
                return output


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
