from app.book import Book
from app.commands import (
    DisplayCommand,
    PrintCommand,
    SerializeCommand
)
from app.strategies import (
    ConsoleDisplay,
    ReverseDisplay,
    ConsolePrint,
    ReversePrint,
    JsonSerializer,
    XmlSerializer
)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    command_map = {
        "display": {
            "console": DisplayCommand(book, ConsoleDisplay()),
            "reverse": DisplayCommand(book, ReverseDisplay())
        },
        "print": {
            "console": PrintCommand(book, ConsolePrint()),
            "reverse": PrintCommand(book, ReversePrint())
        },
        "serialize": {
            "json": SerializeCommand(book, JsonSerializer()),
            "xml": SerializeCommand(book, XmlSerializer())
        }
    }

    for cmd, method_type in commands:
        if cmd in command_map and method_type in command_map[cmd]:
            command = command_map[cmd][method_type]
            result = command.execute()
            if cmd == "serialize":
                return result
        else:
            raise ValueError(
                f"Unknown command or method type: {cmd}, {method_type}"
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
