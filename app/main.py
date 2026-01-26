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


def handle_display(book: Book, method_type: str) -> None:
    printers[method_type].display(book)


def handle_print(book: Book, method_type: str) -> None:
    printers[method_type].print(book)


def handle_serialize(book: Book, method_type: str) -> str:
    return serializers[method_type]().serialize(book)


command_handlers = {
    "display": handle_display,
    "print": handle_print,
    "serialize": handle_serialize,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        handler = command_handlers[cmd]
        result = handler(book, method_type)
        if cmd == "serialize":
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
