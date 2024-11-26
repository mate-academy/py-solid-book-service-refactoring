from app.main_display import (
    Book,
    ConsoleDisplay,
    ConsoleReverse,
    PrintConsole,
    PrintReverse
)
from app.serialize import JsonSerialize, XMLSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    strategies = {
        "display": {
            "console": ConsoleDisplay(),
            "reverse": ConsoleReverse(),
        },
        "print": {
            "console": PrintConsole(),
            "reverse": PrintReverse(),
        },
        "serialize": {
            "json": JsonSerialize(),
            "xml": XMLSerialize(),
        },
    }

    for cmd, method_type in commands:
        if cmd in strategies and method_type in strategies[cmd]:
            strategy = strategies[cmd][method_type]
            if cmd == "serialize":
                return strategy.serialize(book)
            else:
                strategy.display(book)
        else:
            raise ValueError(
                f"Unknown command or method type: {cmd} - {method_type}"
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(
        main(
            sample_book, [("display", "reverse"), ("serialize", "xml")]
        )
    )
