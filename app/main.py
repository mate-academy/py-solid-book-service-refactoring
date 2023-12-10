from app.book import Book
from app.display import DisplayConsole, DisplayReverse
from app.printer import PrinterConsole, PrinterReverse
from app.serializers import JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    main_data = {
        "display": {
            "console": DisplayConsole, "reverse": DisplayReverse
        },
        "print_book": {
            "console": PrinterConsole, "reverse": PrinterReverse
        },
        "serialize": {
            "json": JsonSerializer, "xml": XmlSerializer
        }
    }
    for cmd, method_type in commands:
        if cmd == "display":
            main_data["display"].get(method_type)(book).display()
        elif cmd == "print":
            main_data["print_book"].get(method_type)(book).print_book()
        elif cmd == "serialize":
            return main_data["serialize"].get(method_type)(book).serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
