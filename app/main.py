from app.book import Book
from app.displays import DisplayBookConsole, DisplayBookReverse
from app.printers import PrintBookConsole, PrintBookReverse
from app.serializers import SerializerBookJSON, SerializerBookXML

types = {
    "display": {
        "console": DisplayBookConsole.display,
        "reverse": DisplayBookReverse.display
    },
    "serialize": {
        "json": SerializerBookJSON.serialize,
        "xml": SerializerBookXML.serialize
    },
    "print": {
        "console": PrintBookConsole.print,
        "reverse": PrintBookReverse.print
    }
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd in types and method_type in types[cmd]:
            return types[cmd][method_type](book)
        else:
            raise ValueError(f"Unknown command: {cmd} type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
