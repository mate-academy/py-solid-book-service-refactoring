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


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for command, method_type in commands:
        factory = COMMAND_DISPATCHER[command]
        handler = factory[method_type]()

        if command == "serialize":
            return handler.serialize(book)

        handler_method = getattr(handler, command)
        handler_method(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
