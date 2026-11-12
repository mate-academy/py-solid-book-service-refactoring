from app.book import Book
from app.printer import ConsolePrinter, ReversePrinter
from app.serializer import JSONSerializer, XMLSerializer


SERIALIZERS = {
    "json": JSONSerializer,
    "xml": XMLSerializer,
}

PRINTERS = {
    "console": ConsolePrinter,
    "reverse": ReversePrinter,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "serialize":
            serializer = SERIALIZERS[method_type]()
            return serializer.serialize(book)
        else:
            printer = PRINTERS[method_type]()
            printer.print_book(book, show_title=(cmd != "display"))


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
