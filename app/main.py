from app.book import Book
from app.display import ConsoleDisplay, ReverseDisplay
from app.printer import ConsolePrinter, ReversePrinter
from app.serializer import JSONSerializer, XMLSerializer

BOOK_PROCESSORS = {
    "display": {
        "console": ConsoleDisplay.display_content,
        "reverse": ReverseDisplay.display_content,
    },
    "print": {
        "console": ConsolePrinter.print_book,
        "reverse": ReversePrinter.print_book,
    },
    "serialize": {
        "json": JSONSerializer.serialize_book,
        "xml": XMLSerializer.serialize_book,
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
