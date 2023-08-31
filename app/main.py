from app.book import Book
from app.book_display import ConsoleDisplay, ReverseDisplay
from app.book_printer import ConsolePrinter, ReversePrinter
from app.book_serializer import JSONSerializer, XMLSerializer


display_interfaces = {
    "console": ConsoleDisplay(),
    "reverse": ReverseDisplay(),
}

printer_interfaces = {
    "console": ConsolePrinter(),
    "reverse": ReversePrinter(),
}

serializer_interfaces = {
    "json": JSONSerializer(),
    "xml": XMLSerializer(),
}


def main(
    book: Book,
    commands: list[tuple[str, str]],
) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display_interfaces.get(method_type).display(book)
        elif cmd == "print":
            printer_interfaces.get(method_type).print_book(book)
        elif cmd == "serialize":
            return serializer_interfaces.get(method_type).serialize(book)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
