from app.models import Book
from app.services import (
    DisplayConsole,
    DisplayReverse,
    PrintConsole,
    PrintReverse
)
from app.serializers import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_mapping = {
        "console": DisplayConsole(),
        "reverse": DisplayReverse()
    }

    print_mapping = {
        "console": PrintConsole(),
        "reverse": PrintReverse()
    }

    serialize_mapping = {
        "json": JsonSerializer("json"),
        "xml": XmlSerializer("xml")
    }

    for cmd, method_type in commands:
        if cmd == "display":
            if method_type in display_mapping:
                display_mapping[method_type].display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            if method_type in print_mapping:
                print_mapping[method_type].print_book(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            if method_type in serialize_mapping:
                return serialize_mapping[method_type].serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
