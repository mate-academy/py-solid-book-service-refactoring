from app.books.book import Book
from app.books.serializers import JSONBookSerializer, XMLBookSerializer
from app.books.prints import ReverseBookPrint, ConsoleBookPrint
from app.books.displays import ReverseDisplay, ConsoleDisplay


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    actions = {
        "serialize": {
            "json": JSONBookSerializer.serialize,
            "xml": XMLBookSerializer.serialize,
        },
        "print": {
            "console": ConsoleBookPrint.print,
            "reverse": ReverseBookPrint.print,
        },
        "display": {
            "console": ConsoleDisplay.display,
            "reverse": ReverseDisplay.display,
        },
    }
    for cmd, method_type in commands:
        if cmd in actions and method_type in actions[cmd]:
            method = actions[cmd][method_type]
            return method(book)
        else:
            raise ValueError("Unknown command")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
