from app.models import Book
from app.displays import Displayer, BookDisplayConsole, BookDisplayReverse
from app.printers import Printer, BookPrintConsole, BookPrintReverse
from app.serializers import Serializer, BookSerializerJSON, BookSerializerXML

DISPLAYERS: dict[str, Displayer] = {
    "console": BookDisplayConsole(),
    "reverse": BookDisplayReverse(),
}

PRINTERS: dict[str, Printer] = {
    "console": BookPrintConsole(),
    "reverse": BookPrintReverse(),
}

SERIALIZERS: dict[str, Serializer] = {
    "json": BookSerializerJSON(),
    "xml": BookSerializerXML(),
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type not in DISPLAYERS:
                raise ValueError(f"Unknown display type: {method_type}")
            DISPLAYERS[method_type].display(book)
        elif cmd == "print":
            if method_type not in PRINTERS:
                raise ValueError(f"Unknown print type: {method_type}")
            PRINTERS[method_type].print(book)
        elif cmd == "serialize":
            if method_type not in SERIALIZERS:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return SERIALIZERS[method_type].serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
