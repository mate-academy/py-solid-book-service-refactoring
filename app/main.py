from app.model import Book
from app.display import ConsoleDisplayBook, ReverseDisplayBook
from app.print import ConsoleBookPrinter, ReverseBookPrinter
from app.serializer import JSONBookSerializer, XMLBookSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_strategies = {
        "console": ConsoleDisplayBook(),
        "reverse": ReverseDisplayBook(),
    }

    print_strategies = {
        "console": ConsoleBookPrinter(),
        "reverse": ReverseBookPrinter(),
    }

    serialize_strategies = {
        "json": JSONBookSerializer(),
        "xml": XMLBookSerializer(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            if method_type not in display_strategies:
                raise ValueError(f"Unknown display type: {method_type}")
            display_strategies[method_type].display(book)
        elif cmd == "print":
            if method_type not in print_strategies:
                raise ValueError(f"Unknown print type: {method_type}")
            print_strategies[method_type].print_book(book)
        elif cmd == "serialize":
            if method_type not in serialize_strategies:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serialize_strategies[method_type].serialize(book)
        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
