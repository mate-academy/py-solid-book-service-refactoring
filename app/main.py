from __future__ import annotations

from app.book_model import Book
from app.displaying import BookConsoleDisplayer, BookReverseDisplayer
from app.printing import BookReversePrinter, BookConsolePrinter
from app.serialization import BookXMLSerializer, BookJSONSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    command_mapping = {
        "display": {
            "console": BookConsoleDisplayer.display_instance,
            "reverse": BookReverseDisplayer.display_instance
        },
        "print": {
            "console": BookConsolePrinter.print_instance,
            "reverse": BookReversePrinter.print_instance
        },
        "serialize": {
            "json": BookJSONSerializer.serialize,
            "xml": BookXMLSerializer.serialize
        }

    }

    for cmd, method_type in commands:
        return command_mapping[cmd][method_type](book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
