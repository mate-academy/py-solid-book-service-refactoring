from .models import Book
from .printers import PrinterFactory
from .serializers import SerializerFactory


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    printer_factory = PrinterFactory()
    serializer_factory = SerializerFactory()
    for cmd, method_type in commands:
        if cmd == "display":
            printer = printer_factory.create_display_printer(method_type)
            printer.print(book.title, book.content)
        elif cmd == "print":
            printer = printer_factory.create_print_printer(method_type)
            printer.print(book.title, book.content)
        elif cmd == "serialize":
            serializer = serializer_factory.create_serializer(method_type)
            return serializer.serialize(book.title, book.content)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(
        main(
            sample_book,
            [
                ("display", "reverse"),
                ("print", "console"),
                ("serialize", "xml"),
            ],
        )
    )
