from app.display_methods import ConsoleDisplay, ReverseDisplay
from app.print_methods import ConsolePrint, ReversePrint
from app.serialize_methods import JsonSerialize, XmlSerialize
from app.book_handling import Book


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
        "json": JsonSerialize(),
        "xml": XmlSerialize()
    }

    for cmd, method_type in commands:
        if cmd == "display":
            strategy = display_strategies.get(method_type)
            if strategy is None:
                raise ValueError(f"Unknown display type: {method_type}")
            book.display(strategy)
        elif cmd == "print":
            strategy = print_strategies.get(method_type)
            if strategy is None:
                raise ValueError(f"Unknown print type: {method_type}")
            book.print_book(strategy)
        elif cmd == "serialize":
            strategy = serialize_strategies.get(method_type)
            if strategy is None:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return book.serialize(strategy)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
