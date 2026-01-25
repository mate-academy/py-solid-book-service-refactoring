from app.models import Book
from app.displays import ConsoleDisplay, ReverseDisplay
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    displays = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }

    printers = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter(),
    }

    serializers = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }

    for cmd, method in commands:
        if cmd == "display":
            displays[method].show(book)
        elif cmd == "print":
            printers[method].print(book)
        elif cmd == "serialize":
            return serializers[method].serialize(book)
        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    book = Book("Sample Book", "This is some sample content.")
    print(main(book, [("display", "reverse"), ("serialize", "xml")]))
