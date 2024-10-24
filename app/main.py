from app.book import Book
from app.display_strategy import (
    ConsoleDisplayStrategy,
    ReverseDisplayStrategy,
    DisplayStrategyHandler,
)
from app.print_book_strategy import (
    ConsolePrintBookStrategy,
    ReversePrintBookStrategy,
    PrintBookStrategyHandler,
)
from app.serialize_strategy import (
    JsonSerializeStrategy,
    XmlSerializeStrategy,
    SerializeStrategyHandler,
)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_handler = DisplayStrategyHandler(
        ConsoleDisplayStrategy(), ReverseDisplayStrategy()
    )
    print_handler = PrintBookStrategyHandler(
        ConsolePrintBookStrategy(), ReversePrintBookStrategy()
    )
    serialize_handler = SerializeStrategyHandler(
        JsonSerializeStrategy(), XmlSerializeStrategy()
    )

    for cmd, method_type in commands:
        if cmd == "display":
            display_handler.display(book, method_type)
        elif cmd == "print":
            print_handler.print_book(book, method_type)
        elif cmd == "serialize":
            return serialize_handler.serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
