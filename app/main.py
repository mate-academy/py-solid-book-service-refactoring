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


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type not in DISPLAYERS:
                raise ValueError(f"Unknown display type: {method_type}")
            DISPLAYERS[method_type]().display(book.content)
        elif cmd == "print":
            if method_type not in PRINTERS:
                raise ValueError(f"Unknown print type: {method_type}")
            PRINTERS[method_type]().print_book(book.title, book.content)
        elif cmd == "serialize":
            if method_type not in SERIALIZERS:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return (
                SERIALIZERS[method_type]().serialize(book.title, book.content)
            )
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
