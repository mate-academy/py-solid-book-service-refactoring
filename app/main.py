from app.book import Book
from app.displays import DisplayConsole, DisplayReverse
from app.printers import PrintConsole, PrintReverse
from app.serializers import SerializeJson, SerializeXml

DISPLAY_POSSIBILITIES = {
    "console": DisplayConsole,
    "reverse": DisplayReverse,
}

PRINT_POSSIBILITIES = {
    "console": PrintConsole,
    "reverse": PrintReverse,
}

SERIALIZE_POSSIBILITIES = {
    "json": SerializeJson,
    "xml": SerializeXml,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            DISPLAY_POSSIBILITIES[method_type]().display(book.content)
        elif cmd == "print":
            PRINT_POSSIBILITIES[method_type]().print_book(book)
        elif cmd == "serialize":
            return SERIALIZE_POSSIBILITIES[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
