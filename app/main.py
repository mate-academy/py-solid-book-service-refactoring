from app.book import Book
from app.displayers import ConsoleDisplayer, ReverseDisplayer
from app.printers import ReversePrinter, ConsolePrinter
from app.serializers import JSONSerializer, XMLSerializer


SUPPORTED = {
    "display": {
        "console": ConsoleDisplayer,
        "reverse": ReverseDisplayer,
    },
    "print": {
        "console": ConsolePrinter,
        "reverse": ReversePrinter,
    },
    "serialize": {
        "json": JSONSerializer,
        "xml": XMLSerializer
    }
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_strategy = SUPPORTED.get("display").get(method_type)
            display_strategy(book).display()
        elif cmd == "print":
            printer_strategy = SUPPORTED.get("print").get(method_type)
            printer_strategy(book).print()
        elif cmd == "serialize":
            serializer_strategy = SUPPORTED.get("serialize").get(method_type)
            return serializer_strategy(book).serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
