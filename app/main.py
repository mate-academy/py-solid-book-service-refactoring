from app.models.book import Book
from app.printers.console_printer import ConsolePrinter
from app.printers.reverse_printer import ReversePrinter
from app.serializers.json_serializer import JsonSerializer
from app.serializers.xml_serializer import XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    printers = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter()
    }
    serializers = {
        "json": JsonSerializer(),
        "xml": XmlSerializer()
    }

    for cmd, method_type in commands:
        if cmd in ["display", "print"]:
            printers[method_type].print(book)
        elif cmd == "serialize":
            return serializers[method_type].serialize(book)
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
