from app.book import Book
from app.display_processor import (
    DisplayConsoleProcessor,
    DisplayReverseProcessor
)
from app.print_processor import PrintConsoleProcessor, PrintReverseProcessor
from app.serialize_processor import (
    JSONSerializeProcessor,
    XMLSerializeProcessor
)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                DisplayConsoleProcessor().display(book)
            elif method_type == "reverse":
                DisplayReverseProcessor().display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            if method_type == "console":
                PrintConsoleProcessor().print_book(book)
            elif method_type == "reverse":
                PrintReverseProcessor().print_book(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            if method_type == "json":
                return JSONSerializeProcessor().serialize(book)
            elif method_type == "xml":
                return XMLSerializeProcessor().serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
