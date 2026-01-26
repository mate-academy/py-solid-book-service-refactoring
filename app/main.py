from app.book import Book
from app.printer import (ConsoleFormatter,
                         ReverseFormatter,
                         DetailedPrinter,
                         ReverseDetailedPrinter)
from app.serializer import JSONSerializer, XMLSerializer


DISPLAY_MAP = {
    "console": ConsoleFormatter(),
    "reverse": ReverseFormatter()
}

PRINT_MAP = {
    "console": DetailedPrinter(),
    "reverse": ReverseDetailedPrinter()
}

SERIALIZE_MAP = {
    "json": JSONSerializer(),
    "xml": XMLSerializer()
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            formatter = DISPLAY_MAP.get(method_type)
            if formatter:
                print(formatter.format(book))

        elif cmd == "print":
            printer = PRINT_MAP.get(method_type)
            if printer:
                print(printer.format(book))

        elif cmd == "serialize":
            serializer = SERIALIZE_MAP.get(method_type)
            if serializer:
                return serializer.serialize(book)

    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
