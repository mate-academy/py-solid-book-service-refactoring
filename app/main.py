from app.book import Book
from app.book_display import ConsoleDisplay, ReverseDisplay
from app.book_printer import ConsolePrinter, ReversePrinter
from app.book_serializer import JSONSerializer, XMLSerializer


def main(
    book: Book,
    commands: list[tuple[str, str]],
) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                ConsoleDisplay().display(book)
            elif method_type == "reverse":
                ReverseDisplay().display(book)
        elif cmd == "print":
            if method_type == "console":
                ConsolePrinter().print_book(book)
            elif method_type == "reverse":
                ReversePrinter().print_book(book)
        elif cmd == "serialize":
            if method_type == "json":
                return JSONSerializer().serialize(book)
            elif method_type == "xml":
                return XMLSerializer().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
