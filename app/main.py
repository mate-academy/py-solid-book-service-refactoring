from app.book import Book
from app.printer import ConsolePrinter
from app.serializers import JSONSerializer, XMLSerializer
from app.formatter import SimpleFormatter, ReverseFormatter


printers = {
    "console": ConsolePrinter(SimpleFormatter),
    "reverse": ConsolePrinter(ReverseFormatter),
}

serializers = {
    "json": JSONSerializer,
    "xml": XMLSerializer,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            printers[method_type]().display(book)
        elif cmd == "print":
            printers[method_type]().print(book)
        elif cmd == "serialize":
            return serializers[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
