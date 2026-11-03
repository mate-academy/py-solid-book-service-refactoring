from typing import Dict

from app.interfaces import (
    DisplayStrategy,
    PrintStrategy,
    SerializeStrategy
)
from app.strategies import (
    ConsoleDisplay,
    ReverseDisplay,
    ConsolePrint,
    ReversePrint,
    JsonSerialize,
    XmlSerialize
)


class Book:
    def __init__(
        self,
        title: str,
        content: str,
        display_strategies: Dict[str, DisplayStrategy] | None = None,
        print_strategies: Dict[str, PrintStrategy] | None = None,
        serialize_strategies: Dict[str, SerializeStrategy] | None = None,
    ) -> None:
        self.title = title
        self.content = content

        self._display_strategies = display_strategies or {
            "console": ConsoleDisplay(),
            "reverse": ReverseDisplay(),
        }
        self._print_strategies = print_strategies or {
            "console": ConsolePrint(),
            "reverse": ReversePrint(),
        }
        self._serialize_strategies = serialize_strategies or {
            "json": JsonSerialize(),
            "xml": XmlSerialize(),
        }

    def display(self, display_type: str) -> None:

        try:
            strategy = self._display_strategies[display_type]
        except KeyError:
            raise ValueError(f"Unknown display type: {display_type}")
        strategy.display(self)

    def print_book(self, print_type: str) -> None:
        try:
            strategy = self._print_strategies[print_type]
        except KeyError:
            raise ValueError(f"Unknown print type: {print_type}")
        strategy.print_book(self)

    def serialize(self, serialize_type: str) -> str:
        try:
            strategy = self._serialize_strategies[serialize_type]
        except KeyError:
            raise ValueError(f"Unknown serialize type: {serialize_type}")
        return strategy.serialize(self)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            book.print_book(method_type)
        elif cmd == "serialize":
            return book.serialize(method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
