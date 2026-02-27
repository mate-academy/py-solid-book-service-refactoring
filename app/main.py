from app.models import Book
from app.services import (
    ConsoleFormatter,
    ReverseFormatter,
    JSONSerializer,
    XMLSerializer
)

FORMATTERS = {
    "console": ConsoleFormatter(),
    "reverse": ReverseFormatter()
}
SERIALIZERS = {
    "json": JSONSerializer(),
    "xml": XMLSerializer()
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            formatter = FORMATTERS.get(method_type)
            if not formatter:
                raise ValueError(f"Unknown display type: {method_type}")
            print(formatter.format(book))

        elif cmd == "print":
            formatter = FORMATTERS.get(method_type)
            if not formatter:
                raise ValueError(f"Unknown print type: {method_type}")
            if method_type == "console":
                print(f"Printing the book: {book.title}...")
            elif method_type == "reverse":
                print(f"Printing the book in reverse: {book.title}...")
            print(formatter.format(book))

        elif cmd == "serialize":
            serializer = SERIALIZERS.get(method_type)
            if not serializer:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
