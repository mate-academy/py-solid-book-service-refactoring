from app.books import Book
from app.displays import ConsoleDisplay, ReverseDisplay
from app.prints import ConsolePrinter, ReversePrinter
from app.serializers import JsonSerializer, XmlSerializer


def main(book: Book, actions: list) -> None or str:
    actions_dict = {
        "display": {
            "console": ConsoleDisplay.display,
            "reverse": ReverseDisplay.display,
        },
        "print": {
            "console": ConsolePrinter.print_book,
            "reverse": ReversePrinter.print_book,
        },
        "serialize": {
            "json": JsonSerializer.serialize,
            "xml": XmlSerializer.serialize,
        },
    }

    for action, method in actions:
        if action in actions_dict and method in actions_dict[action]:
            return actions_dict[action][method](book)
        raise ValueError(f"Unknown {action} type: {method}")


if __name__ == "__main__":
    book = Book("Sample Book", "This is some sample content.")
    main(book, [("display", "reverse")])
