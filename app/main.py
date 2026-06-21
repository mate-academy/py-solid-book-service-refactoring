from app.models import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import JSONSerializer, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_registry = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay()
    }

    printer_registry = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter()
    }

    serializer_registry = {
        "json": JSONSerializer(),
        "xml": XMLSerializer()
    }

    for cmd, method_type in commands:
        if cmd == "display":
            if method_type not in display_registry:
                raise ValueError(f"Unknown display type: {method_type}")
            display_registry[method_type].display(book)

        elif cmd == "print":
            if method_type not in printer_registry:
                raise ValueError(f"Unknown print type: {method_type}")
            printer_registry[method_type].print_book(book)

        elif cmd == "serialize":
            if method_type not in serializer_registry:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serializer_registry[method_type].serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
