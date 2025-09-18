from .book import Book
from .serializers import BookJSONSerializer, BookXMLSerializer
from .book_printer import BookPrinterConsole, BookPrinterReverse
from .book_displayer import BookDisplayerConsole, BookDisplayerReverse


BOOK_PROCESSORS = {
    "display": {
        "console": BookDisplayerConsole.display_content,
        "reverse": BookDisplayerReverse.display_content,
    },
    "print": {
        "console": BookPrinterConsole.print_book,
        "reverse": BookPrinterReverse.print_book,
    },
    "serialize": {
        "json": BookJSONSerializer.serialize,
        "xml": BookXMLSerializer.serialize,
    }
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        try:
            process = BOOK_PROCESSORS[cmd][method_type]
            return process(book)
        except ValueError as er:
            print("ValueError", er)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
