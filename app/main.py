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
        if not COMMANDS.get(cmd):
            raise ValueError(f"Unknown command {cmd}")
        current_command_type = current_command.get(method_type)
        if not current_command_type :
            raise ValueError(f"Unknown {cmd} type: {method_type}")

        if cmd == "display":
            current_command_type.display(book)
        elif cmd == "print":
            current_command_type.print(book)
        elif cmd == "serialize":
            return current_command_type.serialize(book)

    return None
