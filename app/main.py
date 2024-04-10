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
            if displayer := SUPPORTED[cmd].get(method_type):
                return displayer(book).display()

        elif cmd == "print":
            if printer := SUPPORTED[cmd].get(method_type):
                return printer(book).print()

        elif cmd == "serialize":
            if serializer := SUPPORTED[cmd].get(method_type):
                return serializer(book).serialize()

        raise ValueError(
            f"Unknown command or method type: {cmd} - {method_type}"
        )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
