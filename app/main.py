from app.book import Book
from app.book_display import BookDisplayConsole, BookDisplayReverse
from app.book_print import BookPrintConsole, BookPrintReverse
from app.book_serialize import BookSerializeJson, BookSerializeXml

COMMANDS_DICTIONARY = {
    "display": {
        "console": BookDisplayConsole.display,
        "reverse": BookDisplayReverse.display,
    },
    "print": {
        "console": BookPrintConsole.print,
        "reverse": BookPrintReverse.print,
    },
    "serialize": {
        "json": BookSerializeJson.serialize,
        "xml": BookSerializeXml.serialize,
    },
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        try:
            return COMMANDS_DICTIONARY[cmd][method_type](book)
        except KeyError:
            print(f"Unknown command or method type: {cmd} or {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
