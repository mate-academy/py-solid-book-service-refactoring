from app.book import Book
from app.display_strategy import (DisplayStrategy,
                                  ConsoleDisplay,
                                  ReverseDisplay)
from app.print_strategy import (PrintStrategy,
                                ConsolePrint,
                                ReversePrint)
from app.serialize_strategy import (SerializeStrategy,
                                    JsonSerialize,
                                    XmlSerialize)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_strategy: DisplayStrategy | None = None
    print_strategy: PrintStrategy | None = None
    serialize_strategy: SerializeStrategy | None = None

    for cmd, method_type in commands:
        if cmd == "display":
            display_strategy = get_display_strategy(method_type)
            if display_strategy:
                display_strategy.display(book.content)
        elif cmd == "print":
            print_strategy = get_print_strategy(method_type)
            if print_strategy:
                print_strategy.print(book.title, book.content)
        elif cmd == "serialize":
            serialize_strategy = get_serialize_strategy(method_type)
            if serialize_strategy:
                return serialize_strategy.serialize(book.title, book.content)


def get_display_strategy(method_type: str) -> DisplayStrategy | None:
    if method_type == "console":
        return ConsoleDisplay()
    elif method_type == "reverse":
        return ReverseDisplay()
    return None


def get_print_strategy(method_type: str) -> PrintStrategy | None:
    if method_type == "console":
        return ConsolePrint()
    elif method_type == "reverse":
        return ReversePrint()
    return None


def get_serialize_strategy(method_type: str) -> SerializeStrategy | None:
    if method_type == "json":
        return JsonSerialize()
    elif method_type == "xml":
        return XmlSerialize()
    return None
