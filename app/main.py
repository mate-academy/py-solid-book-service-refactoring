from app.book.book import Book
from app.book.factories.displayer_factory import DisplayerFactory
from app.book.factories.printer_factory import PrinterFactory
from app.book.factories.serializer_factory import SerializerFactory
from app.book.custom_exceptions.displayer_errors import UnknownDisplayTypeError
from app.book.custom_exceptions.printer_errors import UnknownPrintTypeError
from app.book.custom_exceptions.serializer_errors import (
    UnknownSerializeTypeError
)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    try:
        for cmd, method_type in commands:
            if cmd == "display":
                displayer = DisplayerFactory.get_displayer(method_type)
                displayer.display(book)
            elif cmd == "print":
                printer = PrinterFactory.get_printer(method_type)
                printer.print_book(book)
            elif cmd == "serialize":
                serializer = SerializerFactory.get_serializer(method_type)
                return serializer.serialize(book)
    except (
        UnknownDisplayTypeError,
        UnknownPrintTypeError,
        UnknownSerializeTypeError
    ) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
