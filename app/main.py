from app.models import (
    Book,
    ConsoleDisplay, ReversedDisplay,
    ConsolePrint, ReversedPrint,
    JsonSerializer, XMLSerializer
)

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


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if not DISPLAYS.get(method_type):
                raise ValueError(f"Unknown display type: {method_type}")
            return DISPLAYS[method_type].display(book)

        elif cmd == "print":
            if not PRINTS.get(method_type):
                raise ValueError(f"Unknown print type: {method_type}")
            return PRINTS[method_type].print(book)

        elif cmd == "serialize":
            if not SERIALIZERS.get(method_type):
                raise ValueError(f"Unknown serialize type: {method_type}")
            return SERIALIZERS[method_type].serialize(method_type, book)

    return None
