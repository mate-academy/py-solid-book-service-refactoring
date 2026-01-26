from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.serializers import JsonSerializer, XmlSerializer


DISPLAY_FACTORY = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay,
}

PRINTER_FACTORY = {
    "console": ConsolePrinter,
    "reverse": ReversePrinter,
}

SERIALIZER_FACTORY = {
    "json": JsonSerializer,
    "xml": XmlSerializer,
}

COMMAND_DISPATCHER = {
    "display": DISPLAY_FACTORY,
    "print": PRINTER_FACTORY,
    "serialize": SERIALIZER_FACTORY,
}

COMMAND_METHOD = {
    "display": "show",
    "print": "print",
    "serialize": "serialize",
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for command, method_type in commands:
        handler = COMMAND_DISPATCHER[command][method_type]()
        method_name = COMMAND_METHOD[command]
        method = getattr(handler, method_name)
        result = method(book)

        if result is not None:
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
