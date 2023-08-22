from app.book import Book
from app.displaying import (
    BookDisplayConsole,
    BookDisplayReverse
)
from app.printing import (
    BookPrintConsole,
    BookPrintReverse
)
from app.serializing import (
    BookSerializeJSON,
    BookSerializeXML
)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    displaying = {
        "console": BookDisplayConsole(),
        "reverse": BookDisplayReverse(),
    }

    printing = {
        "console": BookPrintConsole(),
        "reverse": BookPrintReverse(),
    }

    serialization = {
        "json": BookSerializeJSON(),
        "xml": BookSerializeXML(),
    }
    for cmd, method_type in commands:
        if cmd == "display":
            displaying[method_type].display(book.content)
        elif cmd == "print":
            printing[method_type].print(book.title, book.content)
        elif cmd == "serialize":
            return serialization[method_type].serialize(
                book.title,
                book.content
            )


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
