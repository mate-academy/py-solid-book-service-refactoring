from app.models import Book
from app.display import BookConsoleDisplay, BookReverseDisplay
from app.printer import BookConsolePrinter, BookReversePrinter
from app.serializers import BookJsonSerializer, BookXmlSerializer


def serialize_book(book: "Book", method_type: str) -> None | str:
    serializers = {
        "json": BookJsonSerializer(),
        "xml": BookXmlSerializer(),
    }

    serializer = serializers.get(method_type)
    if serializer is None:
        raise ValueError(f"Unknown serializer type: {method_type}")

    return serializer.serialize(book)


def print_book(book: "Book", method_type: str) -> None:
    printers = {
        "console": BookConsolePrinter(),
        "reverse": BookReversePrinter(),
    }

    printer = printers.get(method_type)

    if printer is None:
        raise ValueError(f"Unknown print type: {method_type}")

    printer.print_book(book)


def display_book(book: "Book", method_type: str) -> None:
    displayers = {
        "console": BookConsoleDisplay(),
        "reverse": BookReverseDisplay(),
    }

    displayer = displayers.get(method_type)

    if displayer is None:
        raise ValueError(f"Unknown display type: {method_type}")
    displayer.display(book)


def main(book: Book, commands: list[tuple[str, str]]) -> None:
    for cmd, method_type in commands:
        if cmd == "display":
            display_book(book, method_type)
        elif cmd == "print":
            print_book(book, method_type)
        elif cmd == "serialize":
            return serialize_book(book, method_type)

    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
