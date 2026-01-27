from app.models import Book
from app.displayers import ConsoleDisplayer, ReverseDisplayer
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import JsonSerializer, XmlSerializer


DISPLAYERS = {
    "console": ConsoleDisplayer,
    "reverse": ReverseDisplayer,
}

PRINTERS = {
    "console": ConsolePrinter,
    "reverse": ReversePrinter,
}

SERIALIZERS = {
    "json": JsonSerializer,
    "xml": XmlSerializer,
}


def handle_display(book: Book, method_type: str) -> None:
    if method_type not in DISPLAYERS:
        raise ValueError(f"Unknown display type: {method_type}")
    DISPLAYERS[method_type]().display(book.content)


def handle_print(book: Book, method_type: str) -> None:
    if method_type not in PRINTERS:
        raise ValueError(f"Unknown print type: {method_type}")
    PRINTERS[method_type]().print_book(book.title, book.content)


def handle_serialize(book: Book, method_type: str) -> str:
    if method_type not in SERIALIZERS:
        raise ValueError(f"Unknown serialize type: {method_type}")
    return SERIALIZERS[method_type]().serialize(book.title, book.content)


COMMAND_HANDLERS = {
    "display": handle_display,
    "print": handle_print,
    "serialize": handle_serialize,
}


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    for cmd, method_type in commands:
        handler = COMMAND_HANDLERS.get(cmd)
        if handler:
            result = handler(book, method_type)
            if result is not None:
                return result
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
