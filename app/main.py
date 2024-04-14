from app.model import Book
from app.printer import ConsolePrinter, ReversePrinter
from app.disply import ReverseDisplay, ConsoleDisplay
from app.serializer import XMLSerializer, JSONSerializer


data = {
    "serialize": {
        "json": JSONSerializer,
        "xml": XMLSerializer
    },
    "display": {
        "console": ConsoleDisplay,
        "reverse": ReverseDisplay
    },
    "printer": {
        "console": ConsolePrinter,
        "reverse": ReversePrinter,
    }

}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            data.get("display").get(method_type)(book).display()
        elif cmd == "print":
            data.get("printer").get(method_type)(book).printer()
        elif cmd == "serialize":
            return data.get("serialize").get(method_type)(book).serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
