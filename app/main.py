from app.models import Book
from app.registry import STRATEGIES


def main(
        book: Book,
        commands: list[tuple[str, str]],
        strategies: dict = STRATEGIES
) -> None | str:
    result = None

    for cmd, method_type in commands:
        strategy = strategies.get(cmd, {}).get(method_type)
        if not strategy:
            raise ValueError(f"Unknown {cmd} type: {method_type}")

        if cmd == "display":
            strategy.display(book)
        elif cmd == "print":
            strategy.print_book(book)
        elif cmd == "serialize":
            result = strategy.serialize(book)

    return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(
        main(sample_book, [
            ("display", "reverse"),
            ("serialize", "xml")
        ], STRATEGIES)
    )
