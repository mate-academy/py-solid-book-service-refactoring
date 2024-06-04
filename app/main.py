from app.book import Book
from app.display_book import (
    Displayer,
    BookConsoleDisplayer,
    BookReverseDisplayer
)
from app.print_book import (
    Printer,
    BookConsolePrinter,
    BookReversePrinter
)
from app.serialize_book import (
    Serializer,
    BookJSONSerializer,
    BookXMLSerializer
)


def get_displayer(book: Book, display_type: str) -> Displayer:
    if display_type == "console":
        return BookConsoleDisplayer(book)
    elif display_type == "reverse":
        return BookReverseDisplayer(book)
    raise ValueError(f"Unknown display type: {display_type}")


def get_printer(book: Book, print_type: str) -> Printer:
    if print_type == "console":
        displayer = BookConsoleDisplayer(book)
        return BookConsolePrinter(book, displayer)
    elif print_type == "reverse":
        displayer = BookReverseDisplayer(book)
        return BookReversePrinter(book, displayer)
    raise ValueError(f"Unknown print type: {print_type}")


def get_serializer(book: Book, serialize_type: str) -> Serializer:
    if serialize_type == "json":
        return BookJSONSerializer(book)
    elif serialize_type == "xml":
        return BookXMLSerializer(book)
    raise ValueError(f"Unknown serialize type: {serialize_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            get_displayer(book, method_type).display()
        elif cmd == "print":
            get_printer(book, method_type).print()
        elif cmd == "serialize":
            return get_serializer(book, method_type).serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
