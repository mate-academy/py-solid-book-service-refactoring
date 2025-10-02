from app.book import Book, IBook
from app.display import DisplayConsole, DisplayReverse
from app.printer import ConsolePrinter, ConsoleReversePrinter
from app.serializer import JSONSerializer, XMLSerializer

_DISPLAYS = {
    "console": DisplayConsole(),
    "reverse": DisplayReverse(),
}

_PRINTERS = {
    "console": ConsolePrinter(),
    "reverse": ConsoleReversePrinter(),
}

_SERIALIZERS = {
    "json": JSONSerializer(),
    "xml": XMLSerializer(),
}


def main(book: IBook, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        try:
            if cmd == "display":
                _DISPLAYS[method_type].display(book)
            elif cmd == "print":
                _PRINTERS[method_type].print_book(book)
            elif cmd == "serialize":
                return _SERIALIZERS[method_type].serialize(book)
        except KeyError as error:
            raise ValueError(
                f"Unknown command or method type: {cmd}/{method_type}"
            ) from error
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
