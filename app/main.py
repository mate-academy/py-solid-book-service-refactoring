from app.book import Book
from app.strategies.display import (
    ConsoleBookDisplayStrategy, ReverseBookDisplayStrategy
)
from app.strategies.print import (
    ConsoleBookPrintStrategy, ReverseBookPrintStrategy
)
from app.strategies.serialize import JSONBookSerializer, XMLBookSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_strategies = {
        "console": ConsoleBookDisplayStrategy(),
        "reverse": ReverseBookDisplayStrategy()
    }

    print_strategies = {
        "console": ConsoleBookPrintStrategy(),
        "reverse": ReverseBookPrintStrategy()
    }

    serializers = {
        "json": JSONBookSerializer(),
        "xml": XMLBookSerializer()
    }

    for cmd, method_type in commands:
        if cmd == "display":
            strategy = display_strategies.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown display type: {method_type}")
            strategy.display(book)
        elif cmd == "print":
            strategy = print_strategies.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown print type: {method_type}")
            strategy.print_book(book)
        elif cmd == "serialize":
            serializer = serializers.get(method_type)
            if not serializer:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serializer.serialize(book)
        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    result = main(sample_book, [("display", "reverse"), ("serialize", "xml")])
    if result is not None:
        print(result)
