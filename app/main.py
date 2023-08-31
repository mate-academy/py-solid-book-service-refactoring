from app.book import Book
from app.book_display import ConsoleDisplay, ReverseDisplay
from app.book_printer import ConsolePrinter, ReversePrinter
from app.book_serializer import JSONSerializer, XMLSerializer


actions = {
    "display": {
        "console": ConsoleDisplay,
        "reverse": ReverseDisplay,
    },
    "print": {
        "console": ConsolePrinter,
        "reverse": ReversePrinter,
    },
    "serialize": {
        "json": JSONSerializer,
        "xml": XMLSerializer,
    },
}


def main(
    book: Book,
    commands: list[tuple[str, str]],
) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            actions[cmd].get(method_type)().display(book)
        elif cmd == "print":
            actions[cmd].get(method_type)().print_book(book)
        elif cmd == "serialize":
            return actions[cmd].get(method_type)().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
