from typing import Union
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.serializer import JsonSerializer, XmlSerializer


class Book:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content


# --- Strategy mappings (OCP-friendly) ---
DISPLAY_STRATEGIES = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay,
}

PRINTER_STRATEGIES = {
    "console": ConsolePrinter,
    "reverse": ReversePrinter,
}

SERIALIZER_STRATEGIES = {
    "json": JsonSerializer,
    "xml": XmlSerializer,
}


def main(book: Book, commands: list[tuple[str, str]]) -> Union[None, str]:
    for cmd, method_type in commands:
        # --- Display ---
        if cmd == "display":
            strategy_class = DISPLAY_STRATEGIES.get(method_type)
            if not strategy_class:
                raise ValueError(f"Unknown display type: {method_type}")
            strategy_class().display(book)

        # --- Print ---
        elif cmd == "print":
            strategy_class = PRINTER_STRATEGIES.get(method_type)
            if not strategy_class:
                raise ValueError(f"Unknown print type: {method_type}")
            strategy_class().print_book(book)

        # --- Serialize ---
        elif cmd == "serialize":
            strategy_class = SERIALIZER_STRATEGIES.get(method_type)
            if not strategy_class:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return strategy_class().serialize(book)

    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
