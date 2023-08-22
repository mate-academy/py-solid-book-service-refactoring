from app.book import Book
from app.displays import BookDisplayConsole, BookDisplayReverse
from app.printers import BookPrinterConsole, BookPrinterReverse
from app.serializers import BookSerializerJSON, BookSerializerXML


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                BookDisplayConsole.display(book)
            elif method_type == "reverse":
                BookDisplayReverse.display(book)
        elif cmd == "print":
            if method_type == "console":
                BookPrinterConsole.print(book)
            elif method_type == "reverse":
                BookPrinterReverse.print(book)
        elif cmd == "serialize":
            if method_type == "json":
                return BookSerializerJSON.serialize(book)
            if method_type == "xml":
                return BookSerializerXML.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
