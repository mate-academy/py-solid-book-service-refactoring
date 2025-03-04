from app.commands import ConsoleRepresentation, ReverseRepresentation
from app.models import Book
from app.serializers import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    serializers = {"json": JsonSerializer(), "xml": XmlSerializer()}
    representations = {
        "console": ConsoleRepresentation(),
        "reverse": ReverseRepresentation()
    }

    for cmd, method_type in commands:
        if cmd == "display":
            if method_type in representations:
                representations[method_type].display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            if method_type in representations:
                representations[method_type].print_book(book)
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
