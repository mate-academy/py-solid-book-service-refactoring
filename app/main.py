from app.book import Book
from app.display import DisplayConsole, DisplayReverse
from app.print_book import PrintBookConsole, PrintBookReverse
from app.serialize import JsonSerialize, XmlSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    method = {
        "display": {
            "console": DisplayConsole(),
            "reverse": DisplayReverse()
        },
        "print": {
            "console": PrintBookConsole(),
            "reverse": PrintBookReverse()
        },
        "serialize": {
            "json": JsonSerialize(),
            "xml": XmlSerialize()
        },
    }
    for cmd, method_type in commands:
        try:
            if cmd == "display":
                method[cmd][method_type].display(book)
            elif cmd == "print":
                method[cmd][method_type].print_book(book)
            elif cmd == "serialize":
                return method[cmd][method_type].serialize(book)
        except ValueError:
            print(f"Unknown type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
