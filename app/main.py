from __future__ import annotations

from app.book import Book
from app.displayer import BookConsoleDisplayer, BookReverseDisplayer
from app.printer import BookConsolePrinter, BookReversePrinter
from app.serializer import BookJSONSerializer, BookXMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    action_mapping = {
        "display": {
            "console": BookConsoleDisplayer.display,
            "reverse": BookReverseDisplayer.display
        },
        "print": {
            "console": BookConsolePrinter.print,
            "reverse": BookReversePrinter.print
        },
        "serialize": {
            "json": BookJSONSerializer.serialize,
            "xml": BookXMLSerializer.serialize
        }
    }

    for cmd, method_type in commands:
        if cmd in action_mapping and method_type in action_mapping[cmd]:
            method = action_mapping[cmd][method_type]
            return method(book)
        else:
            raise ValueError(f"Unknown method type: ({method_type})")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
