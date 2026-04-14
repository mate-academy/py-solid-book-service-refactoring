from app.book import Book
from app.serializer import SerializerFactory
from app.printer import PrinterFactory
from app.display import DisplayFactory


class BookService:
    def display(self, book: Book, display_type: str) -> None:
        strategy = DisplayFactory.get_display(display_type)
        strategy.display(book)

    def print_book(self, book: Book, print_type: str) -> None:
        printer = PrinterFactory.get_printer(print_type)
        printer.print_book(book)

    def serialize(self, book: Book, serialize_type: str) -> str:
        serializer = SerializerFactory.get_serializer(serialize_type)
        return serializer.serialize(book)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    service = BookService()

    for cmd, method_type in commands:
        if cmd == "display":
            service.display(book, method_type)
        elif cmd == "print":
            service.print_book(book, method_type)
        elif cmd == "serialize":
            return service.serialize(book, method_type)
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
