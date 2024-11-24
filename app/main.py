from .book import Book
from .display import ConsoleDisplay, ReverseDisplayer
from .printers import ConsolePrinter, ReversePrinter
from .serializers import JsonBookSerializer, XMLBookSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displayers = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplayer(),
    }
    printers = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter(),
    }
    serializers = {
        "json": JsonBookSerializer(),
        "xml": XMLBookSerializer(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            displayer = displayers.get(method_type)
            if not displayer:
                raise ValueError(f"Unknown display type: {method_type}")
            displayer.display(book)
        elif cmd == "print":
            printer = printers.get(method_type)
            if not printer:
                raise ValueError(f"Unknown print type: {method_type}")
            printer.print(book)
        elif cmd == "serialize":
            serializer = serializers.get(method_type)
            if not serializer:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
