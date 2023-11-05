from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.serializer import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    command_map = {
        "display": {
            "console": ConsoleDisplay.display,
            "reverse": ReverseDisplay.display,
        },
        "print": {
            "console": ConsolePrinter.print,
            "reverse": ReversePrinter.print,
        },
        "serialize": {
            "json": JsonSerializer.serialize,
            "xml": XmlSerializer.serialize,
        },
    }

    for cmd, method_type in commands:
        if cmd in command_map and method_type in command_map[cmd]:
            return command_map[cmd][method_type](book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("print", "reverse"), ("serialize", "json")]))
