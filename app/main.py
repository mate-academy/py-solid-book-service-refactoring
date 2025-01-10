from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.serialize import JsonSerialize, XmlSerialize
from app.printing import ConsolePrint, ReversePrint


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_strategies = {
        "console": ConsoleDisplay(),
        "reverse": ReverseDisplay(),
    }
    print_strategies = {
        "console": ConsolePrint(),
        "reverse": ReversePrint(),
    }
    serialize_strategies = {
        "json": JsonSerialize(),
        "xml": XmlSerialize(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            strategy = display_strategies.get(method_type)
            strategy.display(book)
        elif cmd == "print":
            strategy = print_strategies.get(method_type)
            strategy.print_book(book)
        elif cmd == "serialize":
            strategy = serialize_strategies.get(method_type)
            return strategy.serialize(book)
        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
