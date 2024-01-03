from app.serializers_for_book import JsonSerialize, XmlSerialize
from app.prints_for_book import ConsolePrint, ReversePrint
from app.displays_for_book import ConsoleDisplay, ReverseDisplay
from app.book_class import Book


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
            "json": JsonSerialize.serialize,
            "xml": XmlSerialize.serialize
        }
    }
    for cmd, method_type in commands:
        if cmd in action and method_type in action[cmd]:
            method = action[cmd][method_type]
            return method(book)
        else:
            raise ValueError("Unknown command or method type: "
                             f"Command({cmd}), Method({method_type})")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
