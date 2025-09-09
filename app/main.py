from .models import Book
from .strategies import ConsoleDisplay, ReverseDisplay
from .printers import ConsolePrinter, ReversePrinter
from .serializers import JsonSerializer, XmlSerializer


DISPLAY_REGISTRY = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay,
}

PRINT_REGISTRY = {
    "console": ConsolePrinter,
    "reverse": ReversePrinter,
}

SERIALIZE_REGISTRY = {
    "json": JsonSerializer,
    "xml": XmlSerializer,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type not in DISPLAY_REGISTRY:
                raise ValueError(f"Unknown display type: {method_type}")
            strategy = DISPLAY_REGISTRY[method_type]()
            print(strategy.render(book))

        elif cmd == "print":
            if (method_type not in PRINT_REGISTRY
                    or method_type not in DISPLAY_REGISTRY):
                raise ValueError(f"Unknown print type: {method_type}")
            printer = PRINT_REGISTRY[method_type]()
            strategy = DISPLAY_REGISTRY[method_type]()
            printer.print(book, strategy)

        elif cmd == "serialize":
            if method_type not in SERIALIZE_REGISTRY:
                raise ValueError(f"Unknown serialize type: {method_type}")
            serializer = SERIALIZE_REGISTRY[method_type]()
            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
