from .book import Book
from .display import DisplayFactory
from .printer import PrinterFactory
from .serializer import SerializerFactory


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display = DisplayFactory.create_display(method_type)
            display.display(book)
        elif cmd == "print":
            printer = PrinterFactory.create_printer(method_type)
            printer.print_book(book)
        elif cmd == "serialize":
            serializer = SerializerFactory.create_serializer(method_type)
            return serializer.serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
