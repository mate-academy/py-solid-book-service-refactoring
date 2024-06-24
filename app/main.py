from app.book_model import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.serializer import JsonSerializer, XmlSerializer
from app.print_strategy import ConsolePrint, ReversePrint


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_strategies = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay()
    }

    print_strategies = {
        "console": ConsolePrint(),
        "reverse": ReversePrint()
    }

    serialize_strategies = {
        "json": JsonSerializer(),
        "xml": XmlSerializer()
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
                strategy.print(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            strategy = serialize_strategies.get(method_type)
            if strategy:
                return strategy.serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
