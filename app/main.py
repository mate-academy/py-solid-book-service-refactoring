from app.book import Book
from app.displays import DisplayConsole, DisplayReverse
from app.printers import PrintBookConsole, PrintBookReverse
from app.serializers import SerializerJson, SerializerXml


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    operation = {
        "display":
            {
                "console": DisplayConsole.display,
                "reverse": DisplayReverse.display
            },
        "print":
            {
                "console": PrintBookConsole.print_book,
                "reverse": PrintBookReverse.print_book
            },
        "serialize":
            {
                "json": SerializerJson.serialize,
                "xml": SerializerXml.serialize
            },
    }

    for cmd, method_type in commands:
        if cmd in operation:
            if method_type in operation[cmd]:
                method = operation[cmd][method_type]
                return method(book)
            raise ValueError(f"Unknown method type: ({method_type})")
        raise ValueError(f"Unknown command: ({cmd})")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
