from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrint, ReversePrint
from app.serializer import JSONSerializer, XMLSerializer


def get_display_strategy(
        strategy_type: str
) -> ConsoleDisplay | ReverseDisplay:
    match strategy_type:
        case "console":
            return ConsoleDisplay()
        case "reverse":
            return ReverseDisplay()
        case _:
            raise ValueError(f"Unknown display type: {strategy_type}")


def get_print_strategy(
        strategy_type: str
) -> ConsolePrint | ReversePrint:
    match strategy_type:
        case "console":
            return ConsolePrint()
        case "reverse":
            return ReversePrint()
        case _:
            raise ValueError(f"Unknown print type: {strategy_type}")


def get_serializer_strategy(
        strategy_type: str
) -> JSONSerializer | XMLSerializer:
    match strategy_type:
        case "json":
            return JSONSerializer()
        case "xml":
            return XMLSerializer()
        case _:
            raise ValueError(f"Unknown serialize type: {strategy_type}")


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            strategy = get_display_strategy(method_type)
            strategy.display(book)
        elif cmd == "print":
            strategy = get_print_strategy(method_type)
            strategy.print(book)
        elif cmd == "serialize":
            strategy = get_serializer_strategy(method_type)
            return strategy.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
