from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.serializer import JSONSerializer, XMLSerializer


def main(
        book: Book,
        commands: list[tuple[str, str]],
) -> None | str:
    instructions = {
        "display": {
            "console": ConsoleDisplay,
            "reverse": ReverseDisplay
        },
        "print": {
            "console": ConsolePrinter,
            "reverse": ReversePrinter
        },
        "serialize": {
            "json": JSONSerializer,
            "xml": XMLSerializer
        }
    }
    for cmd, method_type in commands:
        if cmd == "display":
            return instructions[cmd].get(method_type).display(book)
        elif cmd == "print":
            return instructions[cmd].get(method_type).printer(book)
        elif cmd == "serialize":
            return instructions[cmd].get(method_type).serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
