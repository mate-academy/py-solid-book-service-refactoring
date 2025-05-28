from app.model import Book
from app.strategies import (
    ConsolePrint,
    ConsoleDisplay,
    ReverseDisplay,
    ReversePrint,
    JSONSerialize,
    XMLSerialize
)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_strategy = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay()
    }
    print_strategy = {
        "console": ConsolePrint(),
        "reverse": ReversePrint()
    }
    serializers = {
        "json": JSONSerialize(),
        "xml": XMLSerialize()
    }
    for cmd, method_types in commands:
        if cmd == "display":
            strategy = display_strategy.get(method_types)
            if strategy:
                strategy.display(book)
        elif cmd == "print":
            strategy = print_strategy.get(method_types)
            if strategy:
                strategy.print_book(book)
        elif cmd == "serialize":
            serializer = serializers.get(method_types)
            if serializer:
                return serializer.serialize(book)
        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
