from app.book.book import Book

from app.book.display import DisplayConsole, DisplayReverse
from app.book.print import PrintConsole, ReversePrint
from app.book.serialize import JSONSerialize, XMLSerialize


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_map = {
        "console": DisplayConsole(),
        "reverse": DisplayReverse()
    }

    print_map = {
        "console": PrintConsole(),
        "reverse": ReversePrint()
    }

    serialize_map = {
        "json": JSONSerialize(),
        "xml": XMLSerialize()
    }

    for cmd, method_type in commands:
        if cmd == "display":
            if method_type not in display_map:
                raise ValueError(f"Unknown display type: {method_type}")
            display_map[method_type].display(book)
        elif cmd == "print":
            if method_type not in print_map:
                raise ValueError(f"Unknown print type: {method_type}")
            print_map[method_type].print_book(book)
        elif cmd == "serialize":
            if method_type not in serialize_map:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return serialize_map[method_type].serialize(book)
        else:
            raise ValueError(f"Unknown command: {cmd}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
