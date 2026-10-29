from app.book import Book
from app.displayers import ConsoleDisplayer, ReverseDisplayer
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import JsonSerializer, XmlSerializer

DISPLAYERS = {
    "console": ConsoleDisplayer().display,
    "reverse": ReverseDisplayer().display,
}

PRINTERS = {
    "console": ConsolePrinter().print,
    "reverse": ReversePrinter().print,
}

SERIALIZERS = {
    "json": JsonSerializer().serialize,
    "xml": XmlSerializer().serialize,
}

OPERATIONS = {
    "display": DISPLAYERS,
    "print": PRINTERS,
    "serialize": SERIALIZERS,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        operation = OPERATIONS.get(cmd)
        if operation is None:
            continue
        method = operation.get(method_type)
        if method is None:
            continue
        result = method(book)
        if result is not None:
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
