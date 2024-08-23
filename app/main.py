from app.book import Book
from app.display_types import DisplayConsole, DisplayReverse
from app.print_types import PrintConsole, PrintReverse
from app.serializers import JsonSerialize, XmlSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    book_methods = {
        "display": {
            "console": DisplayConsole().display,
            "reverse": DisplayReverse().display,
        },
        "print": {
            "console": PrintConsole().print,
            "reverse": PrintReverse().print,
        },
        "serialize": {
            "json": JsonSerialize().serialize,
            "xml": XmlSerialize().serialize,
        }
    }

    for cmd, method_type in commands:
        result = book_methods.get(cmd, {}).get(method_type)(book)
        if result:
            return result


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
