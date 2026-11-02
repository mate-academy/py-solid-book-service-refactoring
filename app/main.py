from app.book import Book
from app.display_handlers import ConsoleDisplay, ReverseDisplay
from app.print_handlers import ConsolePrint, ReversePrint
from app.serializers import JSONSerializer, XMLSerializer


DISPLAY_MAPPING = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}

PRINT_MAPPING = {
    "console": ConsolePrint(),
    "reverse": ReversePrint(),
}

SERIALIZE_MAPPING = {
    "json": JSONSerializer(),
    "xml": XMLSerializer(),
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            handler = DISPLAY_MAPPING.get(method_type)
            if not handler:
                raise ValueError(f"Unknown display type: {method_type}")
            handler.display(book)

        elif cmd == "print":
            handler = PRINT_MAPPING.get(method_type)
            if not handler:
                raise ValueError(f"Unknown print type: {method_type}")
            handler.print_book(book)

        elif cmd == "serialize":
            handler = SERIALIZE_MAPPING.get(method_type)
            if not handler:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return handler.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
