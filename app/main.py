from app.book.display import (
    ConsoleDisplay,
    ReverseDisplay
)
from app.book.print_book import (
    ConsolePrint,
    ReversePrint
)
from app.book.serialize import (
    JSONSerialize,
    XMLSerialize
)
from app.book.book import Book


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    actions = {
        "display": {
            "console": ConsoleDisplay(),
            "reverse": ReverseDisplay()
        },
        "print": {
            "console": ConsolePrint(),
            "reverse": ReversePrint()
        },
        "serialize": {
            "json": JSONSerialize(),
            "xml": XMLSerialize()
        }
    }

    for cmd, method_type in commands:
        if cmd == "display":
            if method_type not in actions["display"]:
                raise ValueError(f"Unknown display type: {method_type}")
            actions[cmd][method_type].display(book)
        elif cmd == "print":
            if method_type not in actions["print"]:
                raise ValueError(f"Unknown print type: {method_type}")
            actions[cmd][method_type].print(book)
        elif cmd == "serialize":
            if method_type not in actions["serialize"]:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return actions[cmd][method_type].serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
