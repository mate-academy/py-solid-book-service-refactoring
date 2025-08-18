from app.display import DisplayConsole, DisplayReverse
from app.models import Book
from app.print_book import PrintConsole, PrintReverse
from app.serialize import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_strategies = {
        "console": DisplayConsole(),
        "reverse": DisplayReverse(),
    }

    print_strategies = {
        "console": PrintConsole(),
        "reverse": PrintReverse(),
    }

    serialize_strategies = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            strategy = display_strategies.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown display method: {method_type}")
            strategy.display(book)

        elif cmd == "print":
            strategy = print_strategies.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown print method: {method_type}")
            strategy.print_book(book)

        elif cmd == "serialize":
            strategy = serialize_strategies.get(method_type)
            if not strategy:
                raise ValueError(f"Unknown serialize method: {method_type}")
            return strategy.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
