from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.serializer import JSONSerializer, XMLSerializer

DISPLAYERS = {"console": ConsoleDisplay, "reverse": ReverseDisplay}
PRINTERS = {"console": ConsolePrinter, "reverse": ReversePrinter}
SERIALIZERS = {"json": JSONSerializer, "xml": XMLSerializer}


def _get(registry: dict, key: str, kind: str) -> str:
    try:
        return registry[key]()
    except KeyError:
        raise ValueError(f"Unknown {kind} type: {key}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            _get(DISPLAYERS, method_type, "display").display(book)
        elif cmd == "print":
            _get(PRINTERS, method_type, "print").print_book(book)
        elif cmd == "serialize":
            return _get(SERIALIZERS, method_type, "serialize").serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
