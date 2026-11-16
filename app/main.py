from app.implementations import displays, printers, serializers
from app.models import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type not in displays:
                raise ValueError(f"Method type {method_type}"
                                 f" not supported for display.")
            displays[method_type]().display(book)
        elif cmd == "print":
            if method_type not in printers:
                raise ValueError(f"Method type {method_type}"
                                 f" not supported for printing.")
            printers[method_type]().print_book(book)
        elif cmd == "serialize":
            if method_type not in serializers:
                raise ValueError(f"Method type {method_type}"
                                 f" not supported for serializing.")
            return serializers[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
