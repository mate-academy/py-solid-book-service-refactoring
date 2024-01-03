from app.book import Book
from app.display import DisplayConsole, DisplayReverse
from app.serializer import SerializerJson, SerializerXml
from app.print_book import ConsolePrint, ReversePrint


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    actions = {
        "display": {
            "reverse": DisplayReverse.display,
            "console": DisplayConsole.display
        },
        "serialize": {
            "xml": SerializerXml.serialize,
            "json": SerializerJson.serialize
        },
        "print": {
            "reverse": ReversePrint.print,
            "console": ConsolePrint.print
        }
    }

    for cmd, method_type in commands:
        if cmd in actions and method_type in actions[cmd]:
            return actions[cmd][method_type](book)
        else:
            raise ValueError(f"Unknown {cmd} type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
