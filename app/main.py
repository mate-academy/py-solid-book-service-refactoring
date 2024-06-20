from app.book import Book
from app.display_strategy import (
    ConsoleDisplayStrategy,
    ReverseDisplayStrategy
)
from app.print_strategy import (
    ConsolePrintStrategy,
    ReversePrintStrategy
)
from app.serialize_strategy import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_strategies = {
        "console": ConsoleDisplayStrategy(),
        "reverse": ReverseDisplayStrategy(),
    }

    print_strategies = {
        "console": ConsolePrintStrategy(),
        "reverse": ReversePrintStrategy(),
    }

    serialize_strategies = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }

    for cmd, method_type in commands:
        strategy = None
        error_type = None

        if cmd == "display":
            strategy = display_strategies.get(method_type)
            error_type = "display"
        elif cmd == "print":
            strategy = print_strategies.get(method_type)
            error_type = "print"
        elif cmd == "serialize":
            strategy = serialize_strategies.get(method_type)
            error_type = "serialize"

        if strategy:
            if cmd == "display":
                strategy.display(book.content)
            elif cmd == "print":
                strategy.print_book(book.title, book.content)
            elif cmd == "serialize":
                return strategy.serialize(book.title, book.content)
        else:
            raise ValueError(f"Unknown {error_type} type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
