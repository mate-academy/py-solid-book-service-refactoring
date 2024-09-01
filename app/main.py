from book.book import Book
from book.display import DisplayConsole, DisplayReverse
from book.print_book import PrinterConsole, PrinterReverse
from book.serializers import JSONSerializer, XMLSerializer


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
                return JSONSerializer().serialize(book)
            elif method_type == "xml":
                return XMLSerializer().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
