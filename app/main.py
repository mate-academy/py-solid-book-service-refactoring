from app.displayers import ConsoleDisplayer, ReverseDisplayer
from app.models import Book
from app.printers import ConsolePrinter, ReversePrinter
from app.serializers import JSONSerializer, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displayer_map = {
        "console": ConsoleDisplayer(),
        "reverse": ReverseDisplayer(),
    }
    printer_map = {"console": ConsolePrinter(), "reverse": ReversePrinter()}
    serializer_map = {"json": JSONSerializer(), "xml": XMLSerializer()}

    for cmd, method_type in commands:
        if cmd == "display":
            if method_type in displayer_map:
                book.display(displayer_map[method_type])
            else:
                raise ValueError(f"Unknown display type: {method_type}")

        elif cmd == "print":
            if method_type in printer_map:
                book.print_book(printer_map[method_type])
            else:
                raise ValueError(f"Unknown print type: {method_type}")

        elif cmd == "serialize":
            if method_type in serializer_map:
                return book.serialize(serializer_map[method_type])
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
