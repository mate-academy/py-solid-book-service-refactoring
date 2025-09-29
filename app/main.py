from app.models import Book
from app.display.console import ConsoleDisplay
from app.display.reverse import ReverseDisplay
from app.printer.console import ConsolePrint
from app.printer.reverse import ReversePrint
from app.serializer.json_serializer import JsonSerializer
from app.serializer.xml_serializer import XmlSerializer


# Strategy registry
DISPLAY_STRATEGIES = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}

PRINT_STRATEGIES = {
    "console": ConsolePrint(),
    "reverse": ReversePrint(),
}

SERIALIZER_STRATEGIES = {
    "json": JsonSerializer(),
    "xml": XmlSerializer(),
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            strategy = DISPLAY_STRATEGIES.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown display type: {method_type}")
            strategy.display(book)

        elif cmd == "print":
            strategy = PRINT_STRATEGIES.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown print type: {method_type}")
            strategy.print_book(book)

        elif cmd == "serialize":
            strategy = SERIALIZER_STRATEGIES.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return strategy.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
