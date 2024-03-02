from app.book import Book
from app.display_book import DisplayConsole, DisplayReverse
from app.print_book import PrintBookToConsole, PrintReverseBook
from app.serialize_book import JsonBookSerializer, XmlBookSerializer

display_class = {
    "console": DisplayConsole,
    "reverse": DisplayReverse,
}
print_class = {
    "console": PrintBookToConsole,
    "reverse": PrintReverseBook,
}
serialize_class = {
    "json": JsonBookSerializer,
    "xml": XmlBookSerializer,
}


def main(
        book: Book,
        commands: list[tuple[str, str]],
) -> None | str:
    for command, method_type in commands:
        try:
            if command == "display":
                display_class[method_type]().display(book)
            elif command == "print":
                print_class[method_type]().print_book(book)
            elif command == "serialize":
                return serialize_class[method_type]().serialize(book)
            else:
                raise ValueError(f"Unknown command: {command}")
        except KeyError:
            raise ValueError(f"Unknown method type: {method_type}")
