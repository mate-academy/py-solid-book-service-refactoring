from app.book import Book
from app.book_content_display import (
    ConsoleContentDisplay,
    ReverseContentDisplay,
)
from app.book_printer import (
    ConsolePrintContentDisplay,
    ReversePrintContentDisplay,
)
from app.book_serializer import (
    JsonBookSerializer,
    XmlBookSerializer,
)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:

    display_strategies = {
        "console": ConsoleContentDisplay(),
        "reverse": ReverseContentDisplay(),
    }

    print_strategies = {
        "console": ConsolePrintContentDisplay(),
        "reverse": ReversePrintContentDisplay(),
    }

    serialize_strategies = {
        "json": JsonBookSerializer(),
        "xml": XmlBookSerializer(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            strategy = display_strategies.get(method_type)
            if strategy:
                strategy.display(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            strategy = print_strategies.get(method_type)
            if strategy:
                strategy.print_book(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            strategy = serialize_strategies.get(method_type)
            if strategy:
                return strategy.serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
        else:
            raise ValueError(f"Unknown command: {cmd}")

    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
