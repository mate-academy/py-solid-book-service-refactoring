from app.book import Book
from app.display_book import ConsoleDisplay, ReverseDisplay
from app.print_book import BookConsolePrint, BookReversePrint
from app.serializer import BookJSONSerializer, BookXMLSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    action = {
        "display": {
            "console": ConsoleDisplay.display,
            "reverse": ReverseDisplay.display
        },
        "print": {
            "console": BookConsolePrint.print,
            "reverse": BookReversePrint.print
        },
        "serialize": {
            "json": BookJSONSerializer.serialize,
            "xml": BookXMLSerializer.serialize
        }
    }
    for cmd, method_type in commands:
        if cmd in action and method_type in action[cmd]:
            method = action[cmd][method_type]
            return method(book)
        else:
            raise ValueError(f"Unknown command or method type: "
                             "Command({cmd}), Method({method_type})")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
