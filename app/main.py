from app.book import Book
from app.displays import ConsoleDisplay, ReverseDisplay
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import JSONBookSerializer, XMLBookSerializer


def serialize_book(book: Book, method_type: str) -> str:
    mappings = {"json": JSONBookSerializer, "xml": XMLBookSerializer}
    serializer = mappings.get(method_type)
    if serializer:
        return serializer(book).data
    else:
        raise ValueError(f"Unknown serialization type: {method_type}")


def print_book(book: Book, method_type: str) -> None:
    mappings = {"console": ConsolePrinter, "reverse": ReversePrinter}
    printer = mappings.get(method_type)
    if printer:
        printer(book).print()
    else:
        raise ValueError(f"Unknown print type: {method_type}")


def display_book(book: Book, method_type: str) -> None:
    mappings = {"console": ConsoleDisplay, "reverse": ReverseDisplay}
    displayer = mappings.get(method_type)
    if displayer:
        displayer(book).display()
    else:
        raise ValueError(f"Unknown display type: {method_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_book(book, method_type)
        elif cmd == "print":
            print_book(book, method_type)
        elif cmd == "serialize":
            return serialize_book(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
