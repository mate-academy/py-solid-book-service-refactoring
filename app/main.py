from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print_book import ConsolePrint, ReverserPrint
from app.serializers import JSONSerializer, XMLSerializer


actions = {
    "display": {
        "console": ConsoleDisplay.display,
        "reverse": ReverseDisplay.display,
    },
    "print": {
        "console": ConsolePrint.print_book,
        "reverse": ReverserPrint.print_book,
    },
    "serialize": {
        "json": JSONSerializer.serialize,
        "xml": XMLSerializer.serialize,
    },
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        try:
            action = actions[cmd][method_type]
        except KeyError:
            raise KeyError(f"Invalid command: {cmd} with method type: {method_type}")

        if cmd == "serialize":
            return action(book)

        action(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
