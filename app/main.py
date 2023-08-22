from app.book import Book
from app.serializers import JSONSerializer, XMLSerializer
from app.utils import (
    ConsoleDisplayBook,
    ConsolePrintBook,
    ReverseDisplayBook,
    ReversePrintBook
)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displays = {
        "console": ConsoleDisplayBook(),
        "reverse": ReverseDisplayBook()
    }

    prints = {
        "console": ConsolePrintBook(),
        "reverse": ReversePrintBook()
    }

    serializers = {
        "json": JSONSerializer(),
        "xml": XMLSerializer()
    }

    for cmd, method_type in commands:
        if cmd == "display":
            if method_type in displays:
                displays[method_type].display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            if method_type in prints:
                prints[method_type].print_book(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            if method_type in serializers:
                return serializers[method_type].serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
