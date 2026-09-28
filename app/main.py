from app.books import Book
from app.displays import ConsoleDisplayer, ReverseDisplayer
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import JSONSerializer, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    mapping = {
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
            "xml": XMLSerializer,
        },
    }

    for cmd, method_type in commands:
        runer = mapping[cmd][method_type]()
        output = runer.run(book)

        if cmd == "serialize":
            return output
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
