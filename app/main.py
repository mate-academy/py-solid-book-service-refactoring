from app.book import Book
from app.display_book import DisplayBookInConsole, DisplayBookInReverse
from app.print_book import PrintBookInConsole, PrintBookInReverse
from app.serialize_book import SerializeBookToJson, SerializeBookToXml


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:

    for cmd, method_type in commands:

        if cmd == "display":
            if method_type == "console":
                DisplayBookInConsole(book)
            elif method_type == "reverse":
                DisplayBookInReverse(book)
            else:
                raise ValueError(f"Unknown display type: {method_type}")

        elif cmd == "print":
            if method_type == "console":
                PrintBookInConsole(book)
            elif method_type == "reverse":
                PrintBookInReverse(book)
            else:
                raise ValueError(f"Unknown print type: {method_type}")

        elif cmd == "serialize":
            if method_type == "json":
                return SerializeBookToJson().serialize(book)
            elif method_type == "xml":
                return SerializeBookToXml().serialize(book)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
