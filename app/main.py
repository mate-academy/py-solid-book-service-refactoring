from app.book import Book
from app.display_book import DisplayConsole, DisplayReverse
from app.print_book import PrintConsoleBook, PrintReverseBook
from app.serialize_book import BookJsonSerialize, BookXMLSerialize

DISPLAY_BOOK = {
    "console": DisplayConsole,
    "reverse": DisplayReverse,
}
PRINT_BOOK = {
    "console": PrintConsoleBook,
    "reverse": PrintReverseBook,
}
SERIALIZE_BOOK = {
    "json": BookJsonSerialize,
    "xml": BookXMLSerialize,
}


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    print(book.content)
    for cmd, method_type in commands:
        if cmd == "display":
            DISPLAY_BOOK[method_type]().display(book)
        elif cmd == "print":
            PRINT_BOOK[method_type]().print_book(book)
        elif cmd == "serialize":
            return SERIALIZE_BOOK[method_type]().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
