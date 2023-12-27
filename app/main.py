from app.display import BookDisplay, BookPrinter
from app.serializers import BookJsonSerializer, BookXmlSerializer
from app.models import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display = BookDisplay(book)
            if method_type == "console":
                display.console_display()
            elif method_type == "reverse":
                display.reverse_display()
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            display = BookPrinter(book)
            if method_type == "console":
                display.console_print()
            elif method_type == "reverse":
                display.reverse_print()
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            if method_type == "json":
                serializer = BookJsonSerializer(book)
            elif method_type == "xml":
                serializer = BookXmlSerializer(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serializer.serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
