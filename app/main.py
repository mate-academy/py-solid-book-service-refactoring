from app.data_models import Book
from app.displays import ConsoleDisplay, ReversedDisplay
from app.printers import ConsolePrint, ReversedPrint
from app.serializers import JsonSerializer, XMLSerializer

DISPLAYS = {
    "console": ConsoleDisplay(),
    "reverse": ReversedDisplay(),
}

PRINTS = {
    "console": ConsolePrint(),
    "reverse": ReversedPrint(),
}

SERIALIZERS = {
    "json": JsonSerializer(),
    "xml": XMLSerializer(),
}

COMMANDS = {
    "display": DISPLAYS,
    "print": PRINTS,
    "serialize": SERIALIZERS,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        current_command = COMMANDS.get(cmd)
        if not current_command:
            raise ValueError(f"Unknown command {cmd}")

        handler = current_command.get(method_type)
        if not handler:
            raise ValueError(f"Unknown {cmd} type: {method_type}")

        method = getattr(handler, cmd)
        result = method(book)

        if result is not None:
            return result

    return None

