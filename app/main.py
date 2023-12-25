from app.book import Book
from app.display import DisplayConsole, DisplayReverse
from app.print_book import ConsolePrint, ReversePrint
from app.serializer import SerializerJSON, SerializerXML


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:

    action = {
        "display": {
            "console": DisplayConsole.display,
            "reverse": DisplayReverse.display
        },
        "print": {
            "console": ConsolePrint.print,
            "reverse": ReversePrint.print
        },
        "serialize": {
            "json": SerializerJSON.serialize,
            "xml": SerializerXML.serialize
        }
    }

    for cmd, method_type in commands:
        if cmd in action and method_type in action[cmd]:
            method = action[cmd][method_type]
            return method(book)
        else:
            raise ValueError(
                f"Unknown Command: {cmd} or Method: {method_type}"
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
