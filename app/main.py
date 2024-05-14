from app.book import Book
from app.display import DisplayConsole, DisplayReverse
from app.printer import PrinterConsole, PrinterReverse
from app.serializer import SerializerJSON, SerializerXML

BOOK_MANAGER = {
    "display": {
        "console": DisplayConsole.display,
        "reverse": DisplayReverse.display,
    },
    "print": {
        "console": PrinterConsole.print_book,
        "reverse": PrinterReverse.print_book,
    },
    "serialize": {
        "json": SerializerJSON.serialize,
        "xml": SerializerXML.serialize,
    }
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        try:
            task = BOOK_MANAGER[cmd][method_type]
            result = task(book)
            if cmd == "serialize":
                return result
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
