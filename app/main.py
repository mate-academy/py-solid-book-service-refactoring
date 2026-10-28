from app.book import Book
from app.book import DISPLAY_STRATEGIES, SERIALIZE_STRATEGIES, PRINT_STRATEGIES


def main(book: Book, command: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in command:
        if cmd == "display":
            strategy = DISPLAY_STRATEGIES.get(method_type)
            if strategy is None:
                raise ValueError(f"Unknown display type: {method_type}")
            strategy.display(book)
        elif cmd == "print":
            strategy = PRINT_STRATEGIES.get(method_type)
            if strategy is None:
                raise ValueError(f"Unknown display type: {method_type}")
            strategy.print_book(book)
        elif cmd == "serialize":
            strategy = SERIALIZE_STRATEGIES.get(method_type)
            if strategy is None:
                raise ValueError(f"Unknown display type: {method_type}")
            return strategy.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    main(sample_book, [("display", "reverse"), ("serialize", "xml")])
