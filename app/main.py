from app.serializer import SerializerFactory
from app.printer import PrinterFactory
from app.display import DisplayFactory


class Book:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def display(self, display_type: str) -> None:
        displays = DisplayFactory.get_display(display_type)
        displays.display(self)

    def print_book(self, print_type: str) -> None:
        printer = PrinterFactory.get_printer(print_type)
        printer.print_book(self)

    def serialize(self, serialize_type: str) -> str:
        serializer = SerializerFactory.get_serializer(serialize_type)
        return serializer.serialize(self)


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            book.display(method_type)
        elif cmd == "print":
            book.print_book(method_type)
        elif cmd == "serialize":
            return book.serialize(method_type)
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
