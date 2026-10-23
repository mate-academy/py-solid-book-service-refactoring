from app.books import Book

from app.serializers import JSONSerializer, XMLSerializer
from app.displayers import ConsoleDisplayer, ReverseDisplayer
from app.printers import ConsolePrinter, ReversePrinter


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                return ConsoleDisplayer().display(book)
            if method_type == "reverse":
                return ReverseDisplayer().display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            if method_type == "console":
                return ConsolePrinter().print(book)
            if method_type == "reverse":
                return ReversePrinter().print(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            if method_type == "json":
                return JSONSerializer().serialize(book)
            if method_type == "xml":
                return XMLSerializer().serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
