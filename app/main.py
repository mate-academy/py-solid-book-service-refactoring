from book.book import Book
from display.display import ConsoleDisplay, ReverseDisplay
from serializers.serializers import JSONSerializer, XMLSerializer
from print_book.print_book import ConsolePrinter, ReversePrinter


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                ConsoleDisplay().display(book.content)
            elif method_type == "reverse":
                ReverseDisplay().display(book.content)

        elif cmd == "print":
            if method_type == "console":
                ConsolePrinter().print(book)
            elif method_type == "reverse":
                ReversePrinter().print(book)

        elif cmd == "serialize":
            if method_type == "json":
                return JSONSerializer().serialize(book)
            elif method_type == "xml":
                return XMLSerializer().serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
