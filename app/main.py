from app.book import Book
from app.book_display_classes import (
    BookConsoleDisplayer,
    BookReverseDisplayer,
)
from app.book_print_classes import BookConsolePrinter, BookReversePrinter
from app.book_serialize_classes import BookSerializerJSON, BookSerializerXML


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displays = {
        "console": BookConsoleDisplayer,
        "reverse": BookReverseDisplayer,
    }
    printers = {
        "console": BookConsolePrinter,
        "reverse": BookReversePrinter,
    }
    serializers = {
        "json": BookSerializerJSON,
        "xml": BookSerializerXML,
    }

    all_method_types = (
        list(displays.keys())
        + list(printers.keys())
        + list(serializers.keys())
    )

    for cmd, method_type in commands:

        if method_type not in all_method_types:
            raise ValueError(f"Unknown method entered: {method_type}.")

        if cmd == "display":
            displays[method_type].display(book)

        elif cmd == "print":
            printers[method_type].print(book)

        elif cmd == "serialize":
            return serializers[method_type].serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
