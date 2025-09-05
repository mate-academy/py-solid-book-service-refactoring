from book import Book
from display import ConsoleDisplay, ReverseDisplay
from printer import ConsolePrinter, ReversePrinter
from serializer import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_strategies = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay()
    }

    print_strategies = {
        "console": ConsolePrinter(),
        "reverse": ReversePrinter()
    }

    serialize_strategies = {
        "json": JsonSerializer(),
        "xml": XmlSerializer()
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
            strategy = serialize_strategies.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return strategy.serialize(book)

    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
