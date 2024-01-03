from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.print import ConsolePrint, ReversePrint
from app.serializer import JSONSerializer, XMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    action = {
        "display": {
            "console": ConsoleDisplay.display,
            "reverse": ReverseDisplay.display
        },
        "print": {
            "console": ConsolePrint.print,
            "reverse": ReversePrint.print
        },
        "serialize": {
            "json": JSONSerializer.serialize,
            "xml": XMLSerializer.serialize
        }
    }

    for cmd, method_type in commands:
        if cmd in action and method_type in action[cmd]:
            method = action[cmd][method_type]
            return method(book)
        raise ValueError(
            f"Unknown Command: {cmd} or Method: {method_type}"
        )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
