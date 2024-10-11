from app.book import Book
from app.book_managers import (
    BookConsolePrinter,
    BookReversePrinter,
    BookConsoleViewer,
    BookReverseViewer, BookJsonSerializer, BookXmlSerializer
)
from app.method_validators import (
    DisplayMethodValidator,
    PrinterMethodValidator,
    SerializerMethodValidator
)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            validator = DisplayMethodValidator()
            validator.validate_method(method_type)
            viewer = BookConsoleViewer(book.title, book.content)

            if method_type == "reverse":
                viewer = BookReverseViewer(book.title, book.content)

            viewer.display()
        elif cmd == "print":
            validator = PrinterMethodValidator()
            validator.validate_method(method_type)
            printer = BookConsolePrinter(book.title, book.content)

            if method_type == "reverse":
                printer = BookReversePrinter(book.title, book.content)

            printer.print()
        elif cmd == "serialize":
            validator = SerializerMethodValidator()
            validator.validate_method(method_type)
            serializer = BookJsonSerializer(book.title, book.content)

            if method_type == "xml":
                serializer = BookXmlSerializer(book.title, book.content)

            return serializer.serialize()


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
