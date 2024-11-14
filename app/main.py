from app.book import Book
from app.display import (
    DisplayBookConsole,
    DisplayBookReverse,
    PrintBookConsole,
    PrintBookReverse
)
from app.serialize import SerializeBookJSON, SerializeBookXML


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                DisplayBookConsole().display_book(book)
            elif method_type == "reverse":
                DisplayBookReverse().display_book(book)
        elif cmd == "print":
            if method_type == "console":
                PrintBookConsole().print_book(book)
            elif method_type == "reverse":
                PrintBookReverse().print_book(book)
        elif cmd == "serialize":
            if method_type == "json":
                return SerializeBookJSON().serialize(book)
            if method_type == "xml":
                return SerializeBookXML().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
