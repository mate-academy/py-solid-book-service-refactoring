from app.services import (
    ConsoleDisplay,
    ReverseDisplay,
    PrintBookConsole,
    PrintBookReverse,
)
from app.serializers import (
    JSONSerializer,
    XMLSerializer
)

from app.book import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_methods = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }
    print_methods = {
        "console": PrintBookConsole(),
        "reverse": PrintBookReverse(),
    }
    serialize_methods = {
        "xml": XMLSerializer(),
        "json": JSONSerializer(),
    }
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type in display_methods:
                display_methods[method_type].display(book)
                continue
            raise ValueError(f"Unknown display type: {method_type}")

        elif cmd == "print":
            if method_type in print_methods:
                print_methods[method_type].book_printing(book)
                continue
            raise ValueError(f"Unknown print type: {method_type}")

        elif cmd == "serialize":
            if method_type in serialize_methods:
                return serialize_methods[method_type].serialize(book)
            raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
