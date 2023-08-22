from app.book import Book
from app.displays import ConsoleDisplay, ReverseDisplay
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import JSONSerializer, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displays = {"console": ConsoleDisplay(), "reverse": ReverseDisplay()}
    printers = {
        "console": ConsolePrinter(), "reverse": ReversePrinter()
    }
    serializers = {"json": JSONSerializer(), "xml": XMLSerializer()}

    for cmd, method_type in commands:
        if cmd == "display":
            display = displays.get(method_type)
            if display:
                display.perform_display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")

        elif cmd == "print":
            printer = printers.get(method_type)
            if printer:
                printer.perform_print(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")

        elif cmd == "serialize":
            serializer = serializers.get(method_type)
            if serializer:
                return serializer.perform_serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
