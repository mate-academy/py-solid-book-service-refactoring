from app.book import Book
from app.display import displays
from app.printers import printers
from app.serializers import serializers


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type not in displays:
                raise ValueError(f"Unknown display type: {method_type}")
            displays[method_type]().display(book.content)

        elif cmd == "print":
            if method_type not in printers:
                raise ValueError(f"Unknown print type: {method_type}")
            printers[method_type]().print_book(book.title, book.content)

        elif cmd == "serialize":
            if method_type not in serializers:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serializers[method_type]().serialize(
                book.title, book.content
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
