from app.Book import Book
from app.display import (
    ConsoleDisplayStrategy,
    ReverseDisplayStrategy
)
from app.printer import ConsolePrintStrategy, ReversePrintStrategy
from app.serializers import JSONSerializer, XMLSerializer


def main(book: Book, actions: list[tuple[str, str]]) -> str | None:
    for action, strategy in actions:
        if action == "display":
            if strategy == "console":
                strategy_instance = ConsoleDisplayStrategy()
            elif strategy == "reverse":
                strategy_instance = ReverseDisplayStrategy()
            else:
                raise ValueError(f"Unknown display strategy: {strategy}")
            book.display(strategy_instance)
        elif action == "print":
            if strategy == "console":
                strategy_instance = ConsolePrintStrategy()
            elif strategy == "reverse":
                strategy_instance = ReversePrintStrategy()
            else:
                raise ValueError(f"Unknown print strategy: {strategy}")
            book.print_book(strategy_instance)
        elif action == "serialize":
            if strategy == "json":
                strategy_instance = JSONSerializer()
            elif strategy == "xml":
                strategy_instance = XMLSerializer()
            else:
                raise ValueError(f"Unknown serialization strategy: {strategy}")
            return book.serialize(strategy_instance)
        else:
            raise ValueError(f"Unknown action: {action}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    result = main(sample_book, [
        ("display", ReverseDisplayStrategy()),
        ("serialize", XMLSerializer())
    ])
    print(result)
