from book.book import (
    Book,
    ConsoleBookPrinter,
    ReverseBookPrinter,
    DisplayConsole,
    ReversDisplayConsole,
)
from serializers.serializers import JSONBookSerializer, XMLBookSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    printers = {
        "console": ConsoleBookPrinter(), "reverse": ReverseBookPrinter()
    }
    displays = {"console": DisplayConsole(), "reverse": ReversDisplayConsole()}
    serializers = {"json": JSONBookSerializer(), "xml": XMLBookSerializer()}

    for cmd, method_type in commands:
        if cmd == "display":
            printer = displays.get(method_type)
            if printer:
                printer.perform_action(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")

        elif cmd == "print":
            printer = printers.get(method_type)
            if printer:
                printer.perform_action(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")

        elif cmd == "serialize":
            serializer = serializers.get(method_type)
            if serializer:
                return serializer.serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
