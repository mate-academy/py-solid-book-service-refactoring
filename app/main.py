from app.displays import ConsoleBookDisplay, ReverseBookDisplay
from app.models import Book
from app.printers import ReverseBookPrinter, ConsoleBookPrinter
from app.serializers import JsonBookSerializer, XmlBookSerializer

COMMANDS = {
    "display": {
        "console": ConsoleBookDisplay.display,
        "reverse": ReverseBookDisplay.display
    },
    "print": {
        "console": ConsoleBookPrinter.print,
        "reverse": ReverseBookPrinter.print
    },
    "serialize": {
        "json": JsonBookSerializer.serialize,
        "xml": XmlBookSerializer.serialize
    }
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd in COMMANDS and method_type in COMMANDS.get(cmd):
            func = COMMANDS.get(cmd).get(method_type)
            return func(book)
        raise ValueError(f"Unknown command: {cmd} type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
