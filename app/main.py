from app.displays import ConsoleDisplay, ReverseDisplay
from app.models import Book
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import JsonSerializer, XmlSerializer

DISPLAY_REGISTRY = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay,
}

PRINTER_REGISTRY = {
    "console": ConsolePrinter,
    "reverse": ReversePrinter,
}

SERIALIZER_REGISTRY = {
    "json": JsonSerializer,
    "xml": XmlSerializer,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    result: str | None = None
    for cmd, method_type in commands:
        if cmd == "display":
            display_cls = DISPLAY_REGISTRY[method_type]
            display = display_cls()
            display.show(book)
        elif cmd == "print":
            printer_cls = PRINTER_REGISTRY[method_type]
            printer = printer_cls()
            printer.print(book)
        elif cmd == "serialize":
            serializer_cls = SERIALIZER_REGISTRY[method_type]
            serializer = serializer_cls()
            result = serializer.serialize(book)

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
