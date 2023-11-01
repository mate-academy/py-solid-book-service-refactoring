from app.book import Book
from app.displays import ConsoleDisplay, ReverseDisplay
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import JSONBookSerializer, XMLBookSerializer


def serialize_book(book: Book, method_type: str) -> str:
    if method_type == "json":
        return JSONBookSerializer(book).data
    elif method_type == "xml":
        return XMLBookSerializer(book).data
    else:
        raise ValueError(f"Unknown serialization type: {method_type}")


def print_book(book: Book, method_type: str) -> None:
    if method_type == "console":
        ConsolePrinter.print(book)
    elif method_type == "reverse":
        ReversePrinter.print(book)
    else:
        raise ValueError(f"Unknown print type: {method_type}")


def display_book(book: Book, method_type: str) -> None:
    if method_type == "console":
        ConsoleDisplay.display(book)
    elif method_type == "reverse":
        ReverseDisplay.display(book)
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
