from app.book import Book
from app.printer import PrinterConsole, PrinterReverse
from app.serializers import SerializerJson, SerializerXml
from app.view import DisplayConsole, DisplayReverse


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                DisplayConsole().display(book)
            elif method_type == "reverse":
                DisplayReverse().display(book)
        elif cmd == "print":
            if method_type == "console":
                PrinterConsole().print_book(book)
            elif method_type == "reverse":
                PrinterReverse().print_book(book)
        elif cmd == "serialize":
            if method_type == "json":
                return SerializerJson().serialize(book)
            elif method_type == "xml":
                return SerializerXml().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [(DisplayConsole().display(sample_book),
                              DisplayReverse().display(sample_book)),
                             ("serialize", "xml")]))
