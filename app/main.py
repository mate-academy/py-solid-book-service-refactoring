from app.book import Book
from app.display_book import DisplayBookInConsole, DisplayBookInReverse
from app.print_book import PrintBookInConsole, PrintBookInReverse
from app.serialize_book import SerializeBookToJson, SerializeBookToXml

COMMANDS_DICTIONARY = {
    "display": {
        "console": DisplayBookInConsole.display,
        "reverse": DisplayBookInReverse.display,
    },
    "print": {
        "console": PrintBookInConsole.print,
        "reverse": PrintBookInReverse.print,
    },
    "serialize": {
        "json": SerializeBookToJson.serialize,
        "xml": SerializeBookToXml.serialize,
    },
}


def main(book: Book, commands: list[tuple[str, str]]) -> str:
    for cmd, method_type in commands:
        try:
            return COMMANDS_DICTIONARY[cmd][method_type](book)
        except KeyError:
            print(f"Unknown command or method type: {cmd} or {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
