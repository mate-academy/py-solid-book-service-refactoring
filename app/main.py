from typing import List, Tuple, Union
from models import Book
from controller import BookController
from strategies import (
    ConsoleDisplay,
    ReverseDisplay,
    ConsolePrint,
    ReversePrint,
    JsonSerialize,
    XmlSerialize,
)


def main(book: Book, commands: List[Tuple[str, str]]) -> Union[None, str]:
    controller = BookController(book)

    strategy_map = {
        "display": {"console": ConsoleDisplay(), "reverse": ReverseDisplay()},
        "print": {"console": ConsolePrint(), "reverse": ReversePrint()},
        "serialize": {"json": JsonSerialize(), "xml": XmlSerialize()},
    }

    for cmd, method_type in commands:
        strategy = strategy_map.get(cmd, {}).get(method_type)
        if not strategy:
            raise ValueError(f"Unknown combination: {cmd} {method_type}")

        if cmd == "display":
            controller.display(strategy)
        elif cmd == "print":
            controller.print_book(strategy)
        elif cmd == "serialize":
            return controller.serialize(strategy)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))

