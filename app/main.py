from .book import Book
from .display_strategy import ConsoleDisplayStrategy, ReverseDisplayStrategy
from .print_strategy import ConsolePrintStrategy, ReversePrintStrategy
from .serialize_strategy import JsonSerializeStrategy, XmlSerializeStrategy


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                strategy = ConsoleDisplayStrategy()
            elif method_type == "reverse":
                strategy = ReverseDisplayStrategy()
            else:
                raise ValueError(f"Unknown display type: {method_type}")
            strategy.display(book.content)
        elif cmd == "print":
            if method_type == "console":
                strategy = ConsolePrintStrategy()
            elif method_type == "reverse":
                strategy = ReversePrintStrategy()
            else:
                raise ValueError(f"Unknown print type: {method_type}")
            strategy.print_book(book.title, book.content)
        elif cmd == "serialize":
            if method_type == "json":
                strategy = JsonSerializeStrategy()
            elif method_type == "xml":
                strategy = XmlSerializeStrategy()
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return strategy.serialize(book.title, book.content)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
