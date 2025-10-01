from app.display import ConsoleDisplay, ReverseDisplay
from app.print import ConsolePrint, ReversePrint
from app.serializers import JsonSerialize, XmlSerialize
from app.book import Book


def main(book: Book, commands: list[tuple[str, str]]) -> str | None:
    options = {
        "display": {
            "console": ConsoleDisplay(),
            "reverse": ReverseDisplay()
        },
        "print": {
            "console": ConsolePrint(),
            "reverse": ReversePrint()
        },
        "serialize": {
            "json": JsonSerialize(),
            "xml": XmlSerialize()
        }
    }

    result = None
    for cmd, method_type in commands:
        if cmd == "display":
            options["display"][method_type].display(book)
        elif cmd == "print":
            options["print"][method_type].print_book(book)
        elif cmd == "serialize":
            result = options["serialize"][method_type].serialize(book)

    return result
