from app.book import Book
from app.display_book import DisplayConsole, DisplayReverse
from app.print_book import PrintBookConsole, PrintBookReverse
from app.serialize_book import SerializeJson, SerializeXml


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    data = {
        "display": {"console": DisplayConsole, "reverse": DisplayReverse},
        "print_book": {"console": PrintBookConsole,
                       "reverse": PrintBookReverse},
        "serialize_book": {"json": SerializeJson, "xml": SerializeXml},
    }

    for cmd, method_type in commands:
        if cmd == "display":
            data["display"].get(method_type)(book).display()
        elif cmd == "print":
            data["print_book"].get(method_type)(book).print_book()
        elif cmd == "serialize":
            return (data["serialize_book"].
                    get(method_type)(book).serialize_book())


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
