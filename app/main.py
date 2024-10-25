from typing import Type

from app.print_book import Book
from app.display import (
    ConsoleDisplay,
    ReverseDisplay,
    DisplayStrategy
)
from app.print_book import (
    ConsolePrint,
    ReversePrint,
    PrintStrategy
)
from app.serialize import (
    JsonSerialize,
    XmlSerialize,
    SerializeStrategy
)


DISPLAY_STRATEGIES: dict[str, Type[DisplayStrategy]] = {
    "console": ConsoleDisplay,
    "reverse": ReverseDisplay,
}

PRINT_STRATEGIES: dict[str, Type[PrintStrategy]] = {
    "console": ConsolePrint,
    "reverse": ReversePrint,
}

SERIALIZER_STRATEGIES: dict[str, Type[SerializeStrategy]] = {
    "json": JsonSerialize,
    "xml": XmlSerialize,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DISPLAY_STRATEGIES[method_type]().display(book)
        elif cmd == "print":
            PRINT_STRATEGIES[method_type]().print(book)
        elif cmd == "serialize":
            return SERIALIZER_STRATEGIES[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
