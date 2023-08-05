from app.book import Book
from app.book_display_classes import (
    BookConsoleDisplayer,
    BookReverseDisplayer,
)
from app.book_print_classes import BookConsolePrinter, BookReversePrinter
from app.book_serialize_classes import BookSerializerJSON, BookSerializerXML


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_methods = ["console", "reverse"]
    print_methods = ["console", "reverse"]
    serialize_methods = ["json", "xml"]
    all_method_types = (display_methods + print_methods + serialize_methods)

    for cmd, method_type in commands:

        if method_type in all_method_types:

            if cmd == "display":
                if method_type == "console":
                    BookConsoleDisplayer.display(book)
                else:
                    BookReverseDisplayer.display(book)

            elif cmd == "print":
                if method_type == "console":
                    BookConsolePrinter.print(book)
                else:
                    BookReversePrinter.print(book)

            elif cmd == "serialize":
                if method_type == "json":
                    return BookSerializerJSON.serialize(book)
                else:
                    return BookSerializerXML.serialize(book)

        else:
            raise ValueError(f"Unknown method type: {method_type}.")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
