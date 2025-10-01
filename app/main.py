from app.book import Book
from app.displays import ConsoleDisplay, ReverseDisplay
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import JSONSerializer, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displays = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }

    printers = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter(),
    }

    serializers = {
        "json": JSONSerializer(),
        "xml": XMLSerializer(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            display = displays.get(method_type)
            if not display:
                raise ValueError(f"Unknown display type: {method_type}")
            display.display(book.content)
        elif cmd == "print":
            printer = printers.get(method_type)
            if not printer:
                raise ValueError(f"Unknown print type: {method_type}")
            printer.print_book(book)
        elif cmd == "serialize":
            serializer = serializers.get(method_type)
            if not serializer:
                raise ValueError(f"Unknown serializer type: {method_type}")
            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
