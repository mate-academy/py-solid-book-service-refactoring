from book.book import (Book,
                       ConsoleBookPrinter,
                       ReverseBookPrinter,
                       DisplayConsole,
                       ReversDisplayConsole,
                       )
from serializers.serializers import JSONBookSerializer, XMLBookSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            if method_type == "console":
                book_printer = DisplayConsole()
            elif method_type == "reverse":
                book_printer = ReversDisplayConsole()
            else:
                raise ValueError(f"Unknown display type: {method_type}")

            book_printer.display_book(book)

        elif cmd == "print":
            if method_type == "console":
                book_printer = ConsoleBookPrinter()
            elif method_type == "reverse":
                book_printer = ReverseBookPrinter()
            else:
                raise ValueError(f"Unknown display type: {method_type}")

            book_printer.print_book(book)

        elif cmd == "serialize":
            if method_type == "json":
                book_serializer = JSONBookSerializer()
            elif method_type == "xml":
                book_serializer = XMLBookSerializer()
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")
            return book_serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
