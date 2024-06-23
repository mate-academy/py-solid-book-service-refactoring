from app.display_strategy import ConsoleDisplayStrategy, ReverseDisplayStrategy
from app.print_book import ConsolePrintStrategy, ReversePrintStrategy
from app.serialize_strategy import JsonSerializeStrategy, XmlSerializeStrategy
from app.book import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    strategies = {
        "display": {
            "console": ConsoleDisplayStrategy(),
            "reverse": ReverseDisplayStrategy(),
        },
        "print": {
            "console": ConsolePrintStrategy(),
            "reverse": ReversePrintStrategy(),
        },
        "serialize": {
            "json": JsonSerializeStrategy(),
            "xml": XmlSerializeStrategy(),
        },
    }

    for cmd, method_type in commands:
        strategy = strategies.get(cmd, {}).get(method_type)
        if not strategy:
            raise ValueError(f"Unknown command {cmd}")

        if cmd == "display":
            strategy.display(book.content)
        elif cmd == "print":
            strategy.print_book(book.title, book.content)
        elif cmd == "serialize":
            return strategy.serialize(book.title, book.content)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
